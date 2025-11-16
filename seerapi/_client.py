from collections.abc import AsyncGenerator
from typing_extensions import Self

from hishel.httpx import AsyncCacheClient
from httpx import URL
from httpx._urls import QueryParams

from seerapi._model_map import MODEL_MAP, ModelInstance, ModelName
from seerapi._models import PagedResponse, PageInfo


def _parse_url_params(url: str) -> QueryParams:
    return URL(url=url).params


def _parse_url_page_info(url: str) -> PageInfo | None:
    if url is None:
        return None

    params = _parse_url_params(url)
    if 'offset' not in params or 'limit' not in params:
        return None

    return PageInfo(
        offset=int(params['offset']),
        limit=int(params['limit']),
    )


class SeerAPI:
    def __init__(
        self,
        *,
        scheme: str = 'https',
        hostname: str = 'api.seerapi.com',
        version_path: str = 'v1',
    ) -> None:
        self.scheme: str = scheme
        self.hostname: str = hostname
        self.version_path: str = version_path
        self.base_url: URL = URL(url=f'{scheme}://{hostname}/{version_path}')
        self._client = AsyncCacheClient(base_url=self.base_url)

    async def __aenter__(self) -> Self:
        """进入异步上下文管理器"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """退出异步上下文管理器，关闭客户端连接"""
        await self.aclose()

    async def aclose(self) -> None:
        """关闭客户端连接并释放资源"""
        await self._client.aclose()

    async def get(self, resource_name: ModelName, id: int) -> ModelInstance:
        model_type = MODEL_MAP[resource_name]
        response = await self._client.get(f'/{resource_name}/{id}')
        response.raise_for_status()
        return model_type.model_validate(response.json())

    async def paginated_list(
        self,
        resource_name: ModelName,
        page_info: PageInfo,
    ) -> PagedResponse[ModelInstance]:
        async def create_generator(
            data: list[dict],
        ) -> AsyncGenerator[ModelInstance, None]:
            for item in data:
                yield await self.get(resource_name, item['id'])

        response = await self._client.get(
            f'/{resource_name}/',
            params={'offset': page_info.offset, 'limit': page_info.limit},
        )
        response.raise_for_status()
        response_json = response.json()
        return PagedResponse(
            count=response.json()['count'],
            results=create_generator(response.json()['results']),
            next=_parse_url_page_info(response_json['next']),
            previous=_parse_url_page_info(response_json['previous']),
            first=_parse_url_page_info(response_json['first']),
            last=_parse_url_page_info(response_json['last']),
        )

    async def list(
        self, resource_name: ModelName
    ) -> AsyncGenerator[ModelInstance, None]:
        """获取所有资源的异步生成器，自动处理分页"""
        page_info = PageInfo(offset=0, limit=100)  # 使用较大的页面大小提高效率

        while True:
            paged_response = await self.paginated_list(resource_name, page_info)

            # 生成当前页的所有结果
            async for item in paged_response.results:
                yield item

            # 检查是否还有下一页
            if paged_response.next is None:
                break

            # 更新到下一页
            page_info = paged_response.next
