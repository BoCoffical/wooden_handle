from PIL import Image
import os
import random

def find_texture(filename):
    cur = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        path = os.path.join(cur, "src", "main", "resources", "assets", "wooden_handle", "textures", "item", filename)
        if os.path.exists(path):
            return path
        cur = os.path.dirname(cur)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "main", "resources", "assets", "wooden_handle", "textures", "item", filename)

INPUT = find_texture("wooden_handle.png")
OUTPUT = os.path.join(os.path.dirname(INPUT), "wooden_handle_optimized.png")

img = Image.open(INPUT).convert("RGBA")
pixels = img.load()

# 1. 木柄主体斑纹（颜色调柔和，90,50,20，增加层次感）
dark_mottle = (90, 50, 20, 255)
for y in range(16):
    for x in range(16):
        r, g, b, a = pixels[x, y]
        if r > 80 and r > g > b and a != 0:
            if random.random() < 0.15:
                pixels[x, y] = dark_mottle

# 2. 三角尖头皮革末端（替代臃肿圆头）
# 我们按从下往上的方式构建三角形，末端只保留最窄的1-2个像素
# 检测棕色像素的右上角区域
for x in range(10, 16):
    for y in range(0, 5):
        r, g, b, a = pixels[x, y]
        if r > 80 and a != 0:  # 属于皮革或木柄
            # 判断是否在皮革头末端（右上区域）
            # 削尖算法：设定有效范围，超出则透明化
            # 比如：最外层（第5格）只有1像素宽度，往里第4格2像素...
            # 根据当前x值确定y的允许范围
            # 假设原矩形在最右侧被削尖
            max_y_allowed = (x - 9)  # 三角形斜率
            if x >= 10 and y > max_y_allowed:
                pixels[x, y] = (0, 0, 0, 0)  # 变成透明，削掉多余部分

# 3. 在三角尖端添加短像素（扎线）
leather_band = (130, 60, 30, 255)  # 暗红棕色
# 直接在最右侧边缘画一条小短线
for y in range(0, 3):
    # 找到最右边缘，填充
    for x in range(15, 10, -1):
        r, g, b, a = pixels[x, y]
        if r > 80 and a != 0:
            pixels[x, y] = leather_band
            break  # 只画在最外面

img.save(OUTPUT)
print(f"木柄纹理已更新（三角尖头）: {OUTPUT}")