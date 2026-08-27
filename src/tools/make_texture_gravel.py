from PIL import Image
import random

img = Image.new('RGBA', (16, 16))
pixels = img.load()

# 调整颜色权重：深灰黑为主，浅灰为高光点缀
# 原版沙砾偏深灰褐，我们增强灰度对比
colors = [
    (55, 55, 55, 255),   # 主深灰（原版中偏多的暗部）
    (85, 85, 85, 255),   # 中等灰
    (120, 120, 120, 255), # 浅灰（少数）
    (30, 30, 30, 255)    # 近黑
]
weights = [45, 35, 15, 5]  # 45%深灰，35%中等，15%浅灰，5%黑

for y in range(16):
    for x in range(16):
        rand = random.random()
        if rand < weights[0]/100:
            pixels[x, y] = colors[0]
        elif rand < (weights[0]+weights[1])/100:
            pixels[x, y] = colors[1]
        elif rand < (weights[0]+weights[1]+weights[2])/100:
            pixels[x, y] = colors[2]
        else:
            pixels[x, y] = colors[3]

# 紫结核：缩小为极小的暗色簇
purple_core = (90, 35, 110, 255)  # 暗紫色
purple_shadow = (50, 20, 60, 255) # 极暗紫

tubercles = [(3, 6), (11, 4), (9, 13)]  # 3个结核点

for cx, cy in tubercles:
    # 撒一点暗紫阴影
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if random.random() < 0.2:
                    pixels[nx, ny] = purple_shadow
    # 中心纯色暗紫点
    pixels[cx, cy] = purple_core

img.save("nodule_gravel.png")
print("结核沙砾已更新（深灰黑基调）")