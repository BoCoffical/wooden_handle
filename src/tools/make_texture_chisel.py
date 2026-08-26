from PIL import Image

# 提亮并减少色差，增加立体感
WOOD_EDGE = (90, 55, 25, 255)
WOOD_CORE = (160, 105, 60, 255)
LEATHER_EDGE = (110, 50, 25, 255)
LEATHER_CORE = (170, 85, 45, 255)

# 铁质改为明亮偏白的钢灰色（完美匹配原版铁剑的质感）
IRON_EDGE = (80, 85, 95, 255)       # 边缘阴影
IRON_MID = (150, 155, 165, 255)     # 主体钢色
IRON_HIGHLIGHT = (215, 220, 230, 255) # 高光

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

        # 2. 皮革缠绳区 (x=8)
        if x == 8 and 14 <= s <= 17:
            if s == 14 or s == 17:
                pixels[x, y] = LEATHER_EDGE
            else:
                pixels[x, y] = LEATHER_CORE
            continue

        # 3. 铁质凿头 (x=9 到 x=13)
        if 9 <= x <= 13 and 14 <= s <= 17:
            if s == 14 or s == 17:
                pixels[x, y] = IRON_EDGE
            else:
                pixels[x, y] = IRON_HIGHLIGHT if x == 13 else IRON_MID
            continue

        # 4. 凿尖 (x=14)
        if x == 14:
            if s == 15 or s == 16:
                pixels[x, y] = IRON_HIGHLIGHT
            elif s == 14:
                pixels[x, y] = IRON_EDGE

img.save('resonance_chisel.png')
print("✅ 共鸣凿纹理已更新：铁头现在像真正的亮银色铁器了！")