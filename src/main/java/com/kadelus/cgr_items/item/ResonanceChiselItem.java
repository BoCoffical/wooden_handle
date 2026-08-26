package com.kadelus.cgr_items.item;

import net.minecraft.entity.LivingEntity;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Hand;
import net.minecraft.util.TypedActionResult;
import net.minecraft.world.World;
import net.minecraft.block.BlockState;
import net.minecraft.util.math.BlockPos;
import net.minecraft.entity.player.PlayerEntity;

public class ResonanceChiselItem extends Item {

    public ResonanceChiselItem(Settings settings) {
        super(settings);
    }

    // 攻击消耗：1点耐久（1.21.1 标准方法，返回 void）
    @Override
    public void hurtEnemy(ItemStack stack, LivingEntity target, LivingEntity attacker) {
        stack.damage(1, attacker, (livingEntity) -> {
            // 这里的 lambda 直接处理丢耐久逻辑，避免了类型歧义
        });
    }

    // 破坏方块（也算攻击）：消耗1点耐久（1.21.1 标准方法，返回 void）
    @Override
    public void mineBlock(ItemStack stack, World world, BlockState state, BlockPos pos, LivingEntity miner) {
        stack.damage(1, miner, (livingEntity) -> {
        });
    }

    // 交互（右键使用）：消耗2点耐久
    @Override
    public TypedActionResult<ItemStack> use(World world, PlayerEntity user, Hand hand) {
        ItemStack stack = user.getStackInHand(hand);
        if (!world.isClient) {
            stack.damage(2, user, (livingEntity) -> {
            });
        }
        return TypedActionResult.success(stack, world.isClient());
    }
}