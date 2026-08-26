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
import net.minecraft.entity.EquipmentSlot;

public class ResonanceChiselItem extends Item {

    public ResonanceChiselItem(Settings settings) {
        super(settings);
    }

    // 攻击消耗：1点耐久
    @Override
    public void hurtEnemy(ItemStack stack, LivingEntity target, LivingEntity attacker) {
        // 直接把装备槽位作为常量传入，绕过 Lambda 类型推断报错
        stack.damage(1, attacker, p -> p.sendToolBreakStatus(EquipmentSlot.MAINHAND));
    }

    // 破坏方块（也算攻击）：消耗1点耐久
    @Override
    public void mineBlock(ItemStack stack, World world, BlockState state, BlockPos pos, LivingEntity miner) {
        stack.damage(1, miner, p -> p.sendToolBreakStatus(EquipmentSlot.MAINHAND));
    }

    // 交互（右键使用）：消耗2点耐久
    @Override
    public TypedActionResult<ItemStack> use(World world, PlayerEntity user, Hand hand) {
        ItemStack stack = user.getStackInHand(hand);
        if (!world.isClient) {
            // 根据手持的手判断是主手还是副手
            EquipmentSlot slot = (hand == Hand.MAIN_HAND) ? EquipmentSlot.MAINHAND : EquipmentSlot.OFFHAND;
            stack.damage(2, user, p -> p.sendToolBreakStatus(slot));
        }
        return TypedActionResult.success(stack, world.isClient());
    }
}