package com.kadelus.cgr_items.item;

import com.kadelus.cgr_items.CgrItemsMod;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroups;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class ModItems {

    // 注册木柄物品
    public static final Item WOODEN_HANDLE = registerItem(
            "wooden_handle",
            new Item(new Item.Settings())
    );

    // 注册方法
    private static Item registerItem(String name, Item item) {
        return Registry.register(
                Registries.ITEM,
                Identifier.of(CgrItemsMod.MOD_ID, name),
                item
        );
    }

    // 批量注册
    public static void registerItems() {
        // 添加到"工具"物品栏分组
        ItemGroupEvents.modifyEntriesEvent(ItemGroups.TOOLS).register(entries -> {
            entries.add(WOODEN_HANDLE);
        });

        // 也可以添加到"原料"物品栏
        ItemGroupEvents.modifyEntriesEvent(ItemGroups.INGREDIENTS).register(entries -> {
            entries.add(WOODEN_HANDLE);
        });
    }
}