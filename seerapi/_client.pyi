from collections.abc import AsyncGenerator
from typing import Literal, overload
from typing_extensions import Self

from hishel.httpx import AsyncCacheClient
from httpx import URL
import seerapi_models as M

from seerapi._model_map import ModelInstance, ModelName
from seerapi._models import PagedResponse, PageInfo

class SeerAPI:
    scheme: str
    hostname: str
    version_path: str
    base_url: URL
    _client: AsyncCacheClient

    def __init__(
        self,
        *,
        scheme: str = 'https',
        hostname: str = 'api.seerapi.com',
        version_path: str = 'v1',
    ) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def aclose(self) -> None: ...
    @overload
    async def get(
        self, resource_name: Literal['battle_effect'], id: int
    ) -> M.BattleEffect: ...
    @overload
    async def get(
        self, resource_name: Literal['battle_effect_type'], id: int
    ) -> M.BattleEffectCategoryORM: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_effect'], id: int
    ) -> M.PetEffect: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_effect_group'], id: int
    ) -> M.PetEffectGroup: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_variation'], id: int
    ) -> M.VariationEffect: ...
    @overload
    async def get(
        self, resource_name: Literal['energy_bead'], id: int
    ) -> M.EnergyBead: ...
    @overload
    async def get(self, resource_name: Literal['equip'], id: int) -> M.Equip: ...
    @overload
    async def get(self, resource_name: Literal['suit'], id: int) -> M.Suit: ...
    @overload
    async def get(
        self, resource_name: Literal['equip_type'], id: int
    ) -> M.EquipType: ...
    @overload
    async def get(
        self, resource_name: Literal['equip_effective_occasion'], id: int
    ) -> M.EquipEffectiveOccasion: ...
    @overload
    async def get(self, resource_name: Literal['soulmark'], id: int) -> M.Soulmark: ...
    @overload
    async def get(
        self, resource_name: Literal['soulmark_tag'], id: int
    ) -> M.SoulmarkTagCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['element_type'], id: int
    ) -> M.ElementType: ...
    @overload
    async def get(
        self, resource_name: Literal['element_type_combination'], id: int
    ) -> M.TypeCombination: ...
    @overload
    async def get(self, resource_name: Literal['item'], id: int) -> M.Item: ...
    @overload
    async def get(
        self, resource_name: Literal['item_category'], id: int
    ) -> M.ItemCategory: ...
    @overload
    async def get(self, resource_name: Literal['gem'], id: int) -> M.Gem: ...
    @overload
    async def get(
        self, resource_name: Literal['gem_category'], id: int
    ) -> M.GemCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['gem_generation_category'], id: int
    ) -> M.GemGenCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_activation_item'], id: int
    ) -> M.SkillActivationItem: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_stone'], id: int
    ) -> M.SkillStone: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_stone_category'], id: int
    ) -> M.SkillStoneCategory: ...
    @overload
    async def get(self, resource_name: Literal['mintmark'], id: int) -> M.Mintmark: ...
    @overload
    async def get(
        self, resource_name: Literal['ability_mintmark'], id: int
    ) -> M.AbilityMintmark: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_mintmark'], id: int
    ) -> M.SkillMintmark: ...
    @overload
    async def get(
        self, resource_name: Literal['universal_mintmark'], id: int
    ) -> M.UniversalMintmark: ...
    @overload
    async def get(
        self, resource_name: Literal['mintmark_class'], id: int
    ) -> M.MintmarkClassCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['mintmark_type'], id: int
    ) -> M.MintmarkTypeCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['mintmark_rarity'], id: int
    ) -> M.MintmarkRarityCategory: ...
    @overload
    async def get(self, resource_name: Literal['pet'], id: int) -> M.Pet: ...
    @overload
    async def get(self, resource_name: Literal['pet_class'], id: int) -> M.PetClass: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_gender'], id: int
    ) -> M.PetGenderCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_vipbuff'], id: int
    ) -> M.PetVipBuffCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_mount_type'], id: int
    ) -> M.PetMountTypeCategory: ...
    @overload
    async def get(self, resource_name: Literal['pet_skin'], id: int) -> M.PetSkin: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_skin_category'], id: int
    ) -> M.PetSkinCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_archive_story_entry'], id: int
    ) -> M.PetArchiveStoryEntry: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_archive_story_book'], id: int
    ) -> M.PetArchiveStoryBook: ...
    @overload
    async def get(
        self, resource_name: Literal['pet_encyclopedia_entry'], id: int
    ) -> M.PetEncyclopediaEntry: ...
    @overload
    async def get(self, resource_name: Literal['skill'], id: int) -> M.Skill: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_effect_type'], id: int
    ) -> M.SkillEffectType: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_effect_param'], id: int
    ) -> M.SkillEffectParam: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_hide_effect'], id: int
    ) -> M.SkillHideEffect: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_category'], id: int
    ) -> M.SkillCategory: ...
    @overload
    async def get(
        self, resource_name: Literal['skill_effect_type_tag'], id: int
    ) -> M.SkillEffectTypeTag: ...
    @overload
    async def get(
        self, resource_name: Literal['eid_effect'], id: int
    ) -> M.EidEffect: ...
    async def get(self, resource_name: ModelName, id: int) -> ModelInstance: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['battle_effect'], page_info: PageInfo
    ) -> PagedResponse[M.BattleEffect]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['battle_effect_type'], page_info: PageInfo
    ) -> PagedResponse[M.BattleEffectCategoryORM]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_effect'], page_info: PageInfo
    ) -> PagedResponse[M.PetEffect]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_effect_group'], page_info: PageInfo
    ) -> PagedResponse[M.PetEffectGroup]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_variation'], page_info: PageInfo
    ) -> PagedResponse[M.VariationEffect]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['energy_bead'], page_info: PageInfo
    ) -> PagedResponse[M.EnergyBead]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['equip'], page_info: PageInfo
    ) -> PagedResponse[M.Equip]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['suit'], page_info: PageInfo
    ) -> PagedResponse[M.Suit]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['equip_type'], page_info: PageInfo
    ) -> PagedResponse[M.EquipType]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['equip_effective_occasion'], page_info: PageInfo
    ) -> PagedResponse[M.EquipEffectiveOccasion]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['soulmark'], page_info: PageInfo
    ) -> PagedResponse[M.Soulmark]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['soulmark_tag'], page_info: PageInfo
    ) -> PagedResponse[M.SoulmarkTagCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['element_type'], page_info: PageInfo
    ) -> PagedResponse[M.ElementType]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['element_type_combination'], page_info: PageInfo
    ) -> PagedResponse[M.TypeCombination]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['item'], page_info: PageInfo
    ) -> PagedResponse[M.Item]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['item_category'], page_info: PageInfo
    ) -> PagedResponse[M.ItemCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['gem'], page_info: PageInfo
    ) -> PagedResponse[M.Gem]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['gem_category'], page_info: PageInfo
    ) -> PagedResponse[M.GemCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['gem_generation_category'], page_info: PageInfo
    ) -> PagedResponse[M.GemGenCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_activation_item'], page_info: PageInfo
    ) -> PagedResponse[M.SkillActivationItem]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_stone'], page_info: PageInfo
    ) -> PagedResponse[M.SkillStone]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_stone_category'], page_info: PageInfo
    ) -> PagedResponse[M.SkillStoneCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['mintmark'], page_info: PageInfo
    ) -> PagedResponse[M.Mintmark]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['ability_mintmark'], page_info: PageInfo
    ) -> PagedResponse[M.AbilityMintmark]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_mintmark'], page_info: PageInfo
    ) -> PagedResponse[M.SkillMintmark]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['universal_mintmark'], page_info: PageInfo
    ) -> PagedResponse[M.UniversalMintmark]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['mintmark_class'], page_info: PageInfo
    ) -> PagedResponse[M.MintmarkClassCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['mintmark_type'], page_info: PageInfo
    ) -> PagedResponse[M.MintmarkTypeCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['mintmark_rarity'], page_info: PageInfo
    ) -> PagedResponse[M.MintmarkRarityCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet'], page_info: PageInfo
    ) -> PagedResponse[M.Pet]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_class'], page_info: PageInfo
    ) -> PagedResponse[M.PetClass]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_gender'], page_info: PageInfo
    ) -> PagedResponse[M.PetGenderCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_vipbuff'], page_info: PageInfo
    ) -> PagedResponse[M.PetVipBuffCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_mount_type'], page_info: PageInfo
    ) -> PagedResponse[M.PetMountTypeCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_skin'], page_info: PageInfo
    ) -> PagedResponse[M.PetSkin]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_skin_category'], page_info: PageInfo
    ) -> PagedResponse[M.PetSkinCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_archive_story_entry'], page_info: PageInfo
    ) -> PagedResponse[M.PetArchiveStoryEntry]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_archive_story_book'], page_info: PageInfo
    ) -> PagedResponse[M.PetArchiveStoryBook]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['pet_encyclopedia_entry'], page_info: PageInfo
    ) -> PagedResponse[M.PetEncyclopediaEntry]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill'], page_info: PageInfo
    ) -> PagedResponse[M.Skill]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_effect_type'], page_info: PageInfo
    ) -> PagedResponse[M.SkillEffectType]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_effect_param'], page_info: PageInfo
    ) -> PagedResponse[M.SkillEffectParam]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_hide_effect'], page_info: PageInfo
    ) -> PagedResponse[M.SkillHideEffect]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_category'], page_info: PageInfo
    ) -> PagedResponse[M.SkillCategory]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['skill_effect_type_tag'], page_info: PageInfo
    ) -> PagedResponse[M.SkillEffectTypeTag]: ...
    @overload
    async def paginated_list(
        self, resource_name: Literal['eid_effect'], page_info: PageInfo
    ) -> PagedResponse[M.EidEffect]: ...
    async def paginated_list(
        self, resource_name: ModelName, page_info: PageInfo
    ) -> PagedResponse[ModelInstance]: ...
    @overload
    async def list(self, resource_name: Literal['battle_effect']) -> M.BattleEffect: ...
    @overload
    async def list(
        self, resource_name: Literal['battle_effect_type']
    ) -> M.BattleEffectCategoryORM: ...
    @overload
    async def list(self, resource_name: Literal['pet_effect']) -> M.PetEffect: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_effect_group']
    ) -> M.PetEffectGroup: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_variation']
    ) -> M.VariationEffect: ...
    @overload
    async def list(self, resource_name: Literal['energy_bead']) -> M.EnergyBead: ...
    @overload
    async def list(self, resource_name: Literal['equip']) -> M.Equip: ...
    @overload
    async def list(self, resource_name: Literal['suit']) -> M.Suit: ...
    @overload
    async def list(self, resource_name: Literal['equip_type']) -> M.EquipType: ...
    @overload
    async def list(
        self, resource_name: Literal['equip_effective_occasion']
    ) -> M.EquipEffectiveOccasion: ...
    @overload
    async def list(self, resource_name: Literal['soulmark']) -> M.Soulmark: ...
    @overload
    async def list(
        self, resource_name: Literal['soulmark_tag']
    ) -> M.SoulmarkTagCategory: ...
    @overload
    async def list(self, resource_name: Literal['element_type']) -> M.ElementType: ...
    @overload
    async def list(
        self, resource_name: Literal['element_type_combination']
    ) -> M.TypeCombination: ...
    @overload
    async def list(self, resource_name: Literal['item']) -> M.Item: ...
    @overload
    async def list(self, resource_name: Literal['item_category']) -> M.ItemCategory: ...
    @overload
    async def list(self, resource_name: Literal['gem']) -> M.Gem: ...
    @overload
    async def list(self, resource_name: Literal['gem_category']) -> M.GemCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['gem_generation_category']
    ) -> M.GemGenCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_activation_item']
    ) -> M.SkillActivationItem: ...
    @overload
    async def list(self, resource_name: Literal['skill_stone']) -> M.SkillStone: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_stone_category']
    ) -> M.SkillStoneCategory: ...
    @overload
    async def list(self, resource_name: Literal['mintmark']) -> M.Mintmark: ...
    @overload
    async def list(
        self, resource_name: Literal['ability_mintmark']
    ) -> M.AbilityMintmark: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_mintmark']
    ) -> M.SkillMintmark: ...
    @overload
    async def list(
        self, resource_name: Literal['universal_mintmark']
    ) -> M.UniversalMintmark: ...
    @overload
    async def list(
        self, resource_name: Literal['mintmark_class']
    ) -> M.MintmarkClassCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['mintmark_type']
    ) -> M.MintmarkTypeCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['mintmark_rarity']
    ) -> M.MintmarkRarityCategory: ...
    @overload
    async def list(self, resource_name: Literal['pet']) -> M.Pet: ...
    @overload
    async def list(self, resource_name: Literal['pet_class']) -> M.PetClass: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_gender']
    ) -> M.PetGenderCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_vipbuff']
    ) -> M.PetVipBuffCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_mount_type']
    ) -> M.PetMountTypeCategory: ...
    @overload
    async def list(self, resource_name: Literal['pet_skin']) -> M.PetSkin: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_skin_category']
    ) -> M.PetSkinCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_archive_story_entry']
    ) -> M.PetArchiveStoryEntry: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_archive_story_book']
    ) -> M.PetArchiveStoryBook: ...
    @overload
    async def list(
        self, resource_name: Literal['pet_encyclopedia_entry']
    ) -> M.PetEncyclopediaEntry: ...
    @overload
    async def list(self, resource_name: Literal['skill']) -> M.Skill: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_effect_type']
    ) -> M.SkillEffectType: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_effect_param']
    ) -> M.SkillEffectParam: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_hide_effect']
    ) -> M.SkillHideEffect: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_category']
    ) -> M.SkillCategory: ...
    @overload
    async def list(
        self, resource_name: Literal['skill_effect_type_tag']
    ) -> M.SkillEffectTypeTag: ...
    @overload
    async def list(self, resource_name: Literal['eid_effect']) -> M.EidEffect: ...
    async def list(
        self, resource_name: ModelName
    ) -> AsyncGenerator[ModelInstance, None]: ...
