package com.kadelus.cgr_items.item;

import com.kadelus.cgr_items.CgrItemsMod;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.component.DataComponentTypes;
import net.minecraft.component.type.AttributeModifiersComponent;
import net.minecraft.entity.attribute.AttributeModifierSlot; // 关键修正：用这个！
import net.minecraft.entity.attribute.EntityAttributeModifier;
import net.minecraft.entity.attribute.EntityAttributes;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroups;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class ModItems {
    public static final Item WOODEN_HANDLE = new Item(new Item.Settings());

    public static final Item RESONANCE_CHISEL = new Item(new Item.Settings()
        .maxCount(1)
        .component(DataComponentTypes.ATTRIBUTE_MODIFIERS,
            AttributeModifiersComponent.builder()
                .add(EntityAttributes.GENERIC_ATTACK_DAMAGE,
                    new EntityAttributeModifier(
                        Identifier.of(CgrItemsMod.MOD_ID, "resonance_chisel_damage"),
                        3.0, // 基础攻击1 + 3 = 4伤害
                        EntityAttributeModifier.Operation.ADD_VALUE),
                    AttributeModifierSlot.MAINHAND) // 关键修正：这里也改！
                .build()));

    public static void registerItems() {
        Registry.register(Registries.ITEM,
            Identifier.of(CgrItemsMod.MOD_ID, "wooden_handle"),
            WOODEN_HANDLE);

        Registry.register(Registries.ITEM,
            Identifier.of(CgrItemsMod.MOD_ID, "resonance_chisel"),
            RESONANCE_CHISEL);

        // 将共鸣凿加入工具物品组
        ItemGroupEvents.modifyEntriesEvent(ItemGroups.TOOLS).register(entries -> {
            entries.add(RESONANCE_CHISEL);
        });
    }
}