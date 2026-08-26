package com.kadelus.cgr_items.item;

import net.minecraft.entity.LivingEntity;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.util.ActionResult;
import net.minecraft.util.Hand;
import net.minecraft.util.TypedActionResult; // 1.21.1 中右键用这个，但按官方文档最终修正是 InteractionResultHolder
import net.minecraft.world.World;
import net.minecraft.block.BlockState;
import net.minecraft.util.math.BlockPos;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.util.hit.BlockHitResult; // 修正导入路径

public class ResonanceChiselItem extends Item {

    public ResonanceChiselItem(Settings settings) {
        super(settings);
    }

    // 攻击消耗：1点耐久 (对应官方文档的 hurtEnemy 事件 [citation:2])
    @Override
    public boolean postDamageEntity(ItemStack stack, LivingEntity target, LivingEntity attacker) {
        stack.damage(1, attacker, p -> p.sendToolBreakStatus(attacker.getActiveHand()));
        return true;
    }

    // 破坏方块（也算攻击）：消耗1点耐久 (对应官方文档的 mineBlock 事件 [citation:2])
    @Override
    public boolean postMine(ItemStack stack, World world, BlockState state, BlockPos pos, LivingEntity miner) {
        stack.damage(1, miner, p -> p.sendToolBreakStatus(miner.getActiveHand()));
        return true;
    }

    // 交互（右键使用）：消耗2点耐久 (对应官方文档的 use 事件 [citation:2])
    // 1.21.1 中右键返回的是 InteractionResultHolder，而非 TypedActionResult
    @Override
    public TypedActionResult<ItemStack> use(World world, PlayerEntity user, Hand hand) {
        ItemStack stack = user.getStackInHand(hand);
        if (!world.isClient) {
            stack.damage(2, user, p -> p.sendToolBreakStatus(hand));
        }
        return TypedActionResult.success(stack, world.isClient());
    }
}