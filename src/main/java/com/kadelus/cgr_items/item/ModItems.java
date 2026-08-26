package com.kadelus.cgr_items.item;

import com.kadelus.cgr_items.CgrItemsMod;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.component.DataComponentTypes;
import net.minecraft.component.type.AttributeModifierSlot; // 关键修正：正确的包路径！
import net.minecraft.component.type.AttributeModifiersComponent;
import net.minecraft.entity.attribute.EntityAttributeModifier;
import net.minecraft.entity.attribute.EntityAttributes;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroups;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class ModItems {
    public static final Item WOODEN_HANDLE = new Item(new Item.Settings());

    // 共鸣凿：单体高伤，类似斧头的“戳刺”手感。
    // 伤害：基础1点 + 修正3点 = 4点总伤害。
    // 攻速：0.33秒一次（约3次/秒）。
    // 原版空手攻速是4.0。3.0 - 4.0 = -1.0。
    public static final Item RESONANCE_CHISEL = new ResonanceChiselItem(new Item.Settings()
    .maxCount(1)
    .maxDamage(200) // 耐久设定为200
    .component(DataComponentTypes.ATTRIBUTE_MODIFIERS,
        AttributeModifiersComponent.builder()
            .add(EntityAttributes.GENERIC_ATTACK_DAMAGE,
                new EntityAttributeModifier(
                    Identifier.of(CgrItemsMod.MOD_ID, "resonance_chisel_damage"),
                    3.0,
                    EntityAttributeModifier.Operation.ADD_VALUE),
                AttributeModifierSlot.MAINHAND)
            .add(EntityAttributes.GENERIC_ATTACK_SPEED,
                new EntityAttributeModifier(
                    Identifier.of(CgrItemsMod.MOD_ID, "resonance_chisel_speed"),
                    -1.0, // 3次/秒的攻击
                    EntityAttributeModifier.Operation.ADD_VALUE),
                AttributeModifierSlot.MAINHAND)
            .build()));

    public static void registerItems() {
        Registry.register(Registries.ITEM,
            Identifier.of(CgrItemsMod.MOD_ID, "wooden_handle"),
            WOODEN_HANDLE);

        Registry.register(Registries.ITEM,
            Identifier.of(CgrItemsMod.MOD_ID, "resonance_chisel"),
            RESONANCE_CHISEL);

        ItemGroupEvents.modifyEntriesEvent(ItemGroups.TOOLS).register(entries -> {
            entries.add(RESONANCE_CHISEL);
        });
    }
}