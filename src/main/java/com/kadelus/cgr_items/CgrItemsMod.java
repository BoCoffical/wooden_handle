package com.kadelus.cgr_items;

import net.fabricmc.api.ModInitializer;
import net.minecraft.util.Identifier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CgrItemsMod implements ModInitializer {
    public static final String MOD_ID = "wooden_handle";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    @Override
    public void onInitialize() {
        // 注册物品
        ModItems.registerItems();
        LOGGER.info("凯德勒斯·木柄 物品已注册！");
    }
}