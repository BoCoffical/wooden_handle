from PIL import Image
import os

# ---------- 自动定位纹理路径 ----------
def find_texture(filename):
    cur = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        path = os.path.join(cur, "src", "main", "resources", "assets", "wooden_handle", "textures", "item", filename)
        if os.path.exists(path):
            return path
        cur = os.path.dirname(cur)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

INPUT = find_texture("wooden_handle.png")
OUTPUT = os.path.join(os.path.dirname(INPUT), "wooden_handle_fixed.png")
print(f"读取原图：{INPUT}")

img = Image.open(INPUT).convert("RGBA")
px = img.load()

# ---------- 打印原图右上角（x=8~15，y=0~5）像素矩阵 ----------
print("\n原图右上角像素矩阵 (x=8~15, y=0~5)：")
for y in range(0, 6):
    row = []
    for x in range(8, 16):
        r, g, b, a = px[x, y]
        if a == 0:
            row.append(" . ")
        else:
            row.append(f"{r:03d}")
    print(f"y{y}: {row}")

# ---------- 自动定位木柄末端 ----------
# 木柄是从左下向右上的斜线，末端应在最右上方的非透明像素
# 我们遍历全图，找到 x+y 最大的非透明像素（视为末端）
max_sum = -1
tip_x, tip_y = 8, 5  # 默认值
for y in range(16):
    for x in range(16):
        r, g, b, a = px[x, y]
        if a > 0:
            s = x + y
            if s > max_sum:
                max_sum = s
                tip_x, tip_y = x, y
print(f"\n自动检测到木柄末端坐标：({tip_x}, {tip_y})")

# ---------- 生成尖角（从末端向右上延伸） ----------
# 方向：x+1, y-1（对角方向）
# 定义颜色（皮革色）
LEATHER_LIGHT = (185, 100, 55)
LEATHER_DARK  = (140, 75, 35)

# 生成4个像素
steps = 4
for i in range(1, steps + 1):
    new_x = tip_x + i
    new_y = tip_y - i
    # 确保不越界
    if 0 <= new_x < 16 and 0 <= new_y < 16:
        # 颜色渐变：最靠近末端用暗色，远离用亮色
        if i == 1:
            color = LEATHER_DARK
        else:
            color = LEATHER_LIGHT
        px[new_x, new_y] = (color[0], color[1], color[2], 255)

# ---------- 额外：补一个与末端的连接像素（避免缺失） ----------
# 如果末端已经存在像素，则不需要；否则补一个
if px[tip_x, tip_y][3] == 0:
    px[tip_x, tip_y] = (140, 75, 35, 255)  # 补暗色

# 保存
img.save(OUTPUT)
print(f"\n✅ 居中尖角已生成，输出：{OUTPUT}")
print("请将 wooden_handle_fixed.png 重命名为 wooden_handle.png 后测试。")