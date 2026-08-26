package com.kadelus.cgr_items.item;

import net.minecraft.block.BlockState;
import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Hand;
import net.minecraft.util.TypedActionResult;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;

public class ResonanceChiselItem extends Item {

    public ResonanceChiselItem(Settings settings) {
        super(settings);
    }

    // 攻击实体：消耗 1 点耐久
    @Override
    public boolean postHit(ItemStack stack, LivingEntity target, LivingEntity attacker) {
        stack.damage(1, attacker, (livingEntity) -> {
        });
        return true;
    }

    // 破坏方块：消耗 1 点耐久
    @Override
    public boolean postMine(ItemStack stack, World world, BlockState state, BlockPos pos, LivingEntity miner) {
        stack.damage(1, miner, (livingEntity) -> {
        });
        return true;
    }

    // 交互（右键使用）：消耗 2 点耐久
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