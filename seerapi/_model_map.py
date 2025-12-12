from typing import Literal, TypeAlias, TypeVar

import seerapi_models as M
from seerapi_models.build_model import BaseResModel

NamedModelName: TypeAlias = Literal[
    'achievement',
    'achievement_branch',
    'achievement_category',
    'achievement_type',
    'title',
    'battle_effect',
    'battle_effect_type',
    'pet_effect',
    'pet_effect_group',
    'pet_variation',
    'energy_bead',
    'equip',
    'suit',
    'equip_type',
    'soulmark_tag',
    'element_type',
    'element_type_combination',
    'item',
    'item_category',
    'gem',
    'gem_category',
    'skill_activation_item',
    'skill_stone',
    'skill_stone_category',
    'mintmark',
    'ability_mintmark',
    'skill_mintmark',
    'universal_mintmark',
    'mintmark_class',
    'mintmark_type',
    'pet',
    'pet_gender',
    'pet_vipbuff',
    'pet_mount_type',
    'pet_skin',
    'pet_archive_story_book',
    'pet_encyclopedia_entry',
    'skill',
    'skill_hide_effect',
    'skill_category',
    'skill_effect_type_tag',
]

# 所有可用的模型路径名称
ModelName: TypeAlias = Literal[
    NamedModelName,
    'equip_effective_occasion',
    'soulmark',
    'gem_generation_category',
    'mintmark_rarity',
    'pet_class',
    'pet_skin_category',
    'pet_archive_story_entry',
    'skill_effect_type',
    'skill_effect_param',
    'eid_effect',
]

ModelInstance: TypeAlias = BaseResModel
NamedModelInstance: TypeAlias = (
    M.Achievement
    | M.AchievementBranch
    | M.AchievementCategory
    | M.AchievementType
    | M.Title
    | M.BattleEffect
    | M.BattleEffectCategory
    | M.PetEffect
    | M.PetEffectGroup
    | M.VariationEffect
    | M.EnergyBead
    | M.Equip
    | M.Suit
    | M.EquipType
    | M.SoulmarkTagCategory
    | M.ElementType
    | M.TypeCombination
    | M.Item
    | M.ItemCategory
    | M.Gem
    | M.GemCategory
    | M.SkillActivationItem
    | M.SkillStone
    | M.SkillStoneCategory
    | M.Mintmark
    | M.AbilityMintmark
    | M.SkillMintmark
    | M.UniversalMintmark
    | M.MintmarkClassCategory
    | M.MintmarkTypeCategory
    | M.Pet
    | M.PetGenderCategory
    | M.PetVipBuffCategory
    | M.PetMountTypeCategory
    | M.PetSkin
    | M.PetArchiveStoryBook
    | M.PetEncyclopediaEntry
    | M.Skill
    | M.SkillHideEffect
    | M.SkillCategory
    | M.SkillEffectTypeTag
)
ModelType: TypeAlias = type[ModelInstance]

T_ModelInstance = TypeVar('T_ModelInstance', bound=ModelInstance)
T_NamedModelInstance = TypeVar('T_NamedModelInstance', bound=NamedModelInstance)

MODEL_MAP: dict[ModelName, ModelType] = {
    'achievement': M.Achievement,
    'achievement_branch': M.AchievementBranch,
    'achievement_category': M.AchievementCategory,
    'achievement_type': M.AchievementType,
    'title': M.Title,
    'battle_effect': M.BattleEffect,
    'battle_effect_type': M.BattleEffectCategory,
    'pet_effect': M.PetEffect,
    'pet_effect_group': M.PetEffectGroup,
    'pet_variation': M.VariationEffect,
    'energy_bead': M.EnergyBead,
    'equip': M.Equip,
    'suit': M.Suit,
    'equip_type': M.EquipType,
    'equip_effective_occasion': M.EquipEffectiveOccasion,
    'soulmark': M.Soulmark,
    'soulmark_tag': M.SoulmarkTagCategory,
    'element_type': M.ElementType,
    'element_type_combination': M.TypeCombination,
    'item': M.Item,
    'item_category': M.ItemCategory,
    'gem': M.Gem,
    'gem_category': M.GemCategory,
    'gem_generation_category': M.GemGenCategory,
    'skill_activation_item': M.SkillActivationItem,
    'skill_stone': M.SkillStone,
    'skill_stone_category': M.SkillStoneCategory,
    'mintmark': M.Mintmark,
    'ability_mintmark': M.AbilityMintmark,
    'skill_mintmark': M.SkillMintmark,
    'universal_mintmark': M.UniversalMintmark,
    'mintmark_class': M.MintmarkClassCategory,
    'mintmark_type': M.MintmarkTypeCategory,
    'mintmark_rarity': M.MintmarkRarityCategory,
    'pet': M.Pet,
    'pet_class': M.PetClass,
    'pet_gender': M.PetGenderCategory,
    'pet_vipbuff': M.PetVipBuffCategory,
    'pet_mount_type': M.PetMountTypeCategory,
    'pet_skin': M.PetSkin,
    'pet_skin_category': M.PetSkinCategory,
    'pet_archive_story_entry': M.PetArchiveStoryEntry,
    'pet_archive_story_book': M.PetArchiveStoryBook,
    'pet_encyclopedia_entry': M.PetEncyclopediaEntry,
    'skill': M.Skill,
    'skill_effect_type': M.SkillEffectType,
    'skill_effect_param': M.SkillEffectParam,
    'skill_hide_effect': M.SkillHideEffect,
    'skill_category': M.SkillCategory,
    'skill_effect_type_tag': M.SkillEffectTypeTag,
    'eid_effect': M.EidEffect,
}
