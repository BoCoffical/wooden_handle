from PIL import Image

img = Image.new('RGBA', (16, 16))
pixels = img.load()

# ---- 8位纯色调色板（高光锐利，阴影深邃） ----
METAL_LIGHT = (240, 245, 255, 255) # 金属高光（极亮银色）
METAL_MID   = (140, 165, 185, 255) # 金属中间调（灰蓝）
METAL_DARK  = (40, 60, 80, 255)    # 金属暗部（深邃深蓝）

BAND_RED    = (160, 90, 55, 255)   # 浅红棕扎带
BAND_DARK   = (90, 50, 25, 255)    # 深棕扎带

WOOD_LIGHT  = (170, 90, 45, 255)   # 木柄高光（亮棕）
WOOD_MID    = (139, 69, 19, 255)   # 木柄中间调
WOOD_DARK   = (60, 30, 10, 255)    # 木柄暗部（深邃暗棕）

# ---- 硬编码：每行(X, Y)的绘制范围 ----
# 严格从左下角(0,15)延伸至右上角(15,0)
path = {
    15: (0, 1),    # 底部圆润收尾（1像素宽）
    14: (0, 3),    # 底部圆润过渡
    13: (0, 5),    # 达到标准5像素宽
    12: (1, 6),
    11: (2, 7),
    10: (3, 8),
    9:  (4, 9),
    8:  (5, 10),
    7:  (6, 11),
    6:  (7, 12),   # 木柄结束（保持5像素宽）
    5:  (8, 13),   # 扎带1（浅红）
    4:  (9, 14),   # 扎带2（深棕）
    3:  (10, 15),  # 凿头开始
    2:  (11, 16),  # 凿头
    1:  (12, 16),  # 凿头尖端收窄
    0:  (13, 16)   # 凿头尖端收尾（锐利尖角）
}

for y, (x_start, x_end) in path.items():
    # 确保x不超过15
    x_end = min(x_end, 15)
    center_x = 15 - y  # 计算中心线坐标
    for x in range(x_start, x_end):
        offset = x - center_x # 负数在左（背光），正数在右（受光）
        abs_offset = abs(offset)

        # 1. 木柄部分 (Y=15 ~ Y=6)
        if y >= 6:
            if abs_offset == 0:
                color = WOOD_LIGHT
            elif abs_offset == 1:
                color = WOOD_MID
            else:
                color = WOOD_DARK

        # 2. 扎带部分 (Y=5 ~ Y=4)
        elif y >= 4:
            if y == 5:
                color = BAND_RED
            else:
                color = BAND_DARK

        # 3. 凿头部分 (Y=3 ~ Y=0)
        else:
            if abs_offset == 0:
                color = METAL_LIGHT
            elif abs_offset == 1:
                # 右侧是受光面，用中间调；左侧是背光面，用暗部
                color = METAL_MID if offset > 0 else METAL_DARK
            else:
                color = METAL_DARK

        # 绘制像素（硬边缘，无抗锯齿）
        pixels[x, y] = color

# 保存
img.save("resonance_chisel.png")
print("完美共鸣凿已生成：5像素宽连续斜线，从左下角延伸至右上角，无任何断层。")