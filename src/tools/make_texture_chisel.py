from PIL import Image

# 沉稳的木材与皮革色（与木柄匹配）
WOOD_EDGE = (100, 65, 35, 255)
WOOD_CORE = (130, 90, 55, 255)
LEATHER_EDGE = (120, 55, 30, 255)
LEATHER_CORE = (150, 75, 45, 255)

# 铁质：降低明度，缩小色差（枪灰色，不乌黑，不泛白）
IRON_EDGE = (55, 58, 66, 255)     # 深灰
IRON_CORE = (95, 98, 108, 255)    # 中间亮灰
IRON_HIGHLIGHT = (120, 125, 135, 255) # 柔和反光

img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
pixels = img.load()

for x in range(16):
    for y in range(16):
        s = x + y

        # 1. 短木柄 (x=2 到 x=7)
        if 2 <= x <= 7 and 14 <= s <= 17:
            if x == 2 and y >= 14: continue
            if s == 14 or s == 17:
                pixels[x, y] = WOOD_EDGE
            else:
                pixels[x, y] = WOOD_CORE
            continue

        # 2. 皮革缠绳区 (x=8)，两层结构强调包裹感
        if x == 8 and 14 <= s <= 17:
            if s == 14 or s == 17:
                pixels[x, y] = LEATHER_EDGE
            else:
                pixels[x, y] = LEATHER_CORE
            continue

        # 3. 加长铁质凿头 (x=9 到 x=13)，宽度保持4像素
        if 9 <= x <= 13 and 14 <= s <= 17:
            # 边缘暗，中间亮，差色小
            if s == 14 or s == 17:
                pixels[x, y] = IRON_EDGE
            else:
                # 靠近尖端的部分稍亮
                if x == 13:
                    pixels[x, y] = IRON_HIGHLIGHT
                else:
                    pixels[x, y] = IRON_CORE
            continue

        # 4. 凿尖 (x=14)，精准斜切收窄
        if x == 14:
            # 尖端的核心亮色，但克制亮度
            if s == 15 or s == 16:
                pixels[x, y] = IRON_HIGHLIGHT
            elif s == 14:
                pixels[x, y] = IRON_EDGE
            # 其他留空

img.save('resonance_chisel.png')
print("✅ 共鸣凿已优化：加长铁头，缩小色差，皮革过渡自然。")