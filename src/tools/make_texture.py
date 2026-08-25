from PIL import Image, ImageDraw
import os

# 定义脚本所在目录的上一级（src/tools -> src）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建目标文件完整路径
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'main', 'resources', 'assets', 'wooden_handle', 'textures', 'item')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'wooden_handle.png')

# 自动创建目录（如果不存在）
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 创建16x16透明画布
img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# 定义颜色
WOOD_DARK = (75, 55, 35, 255)      # 深棕色
WOOD_MID  = (95, 70, 45, 255)      # 中棕色
LEATHER   = (140, 100, 70, 255)    # 皮革色
LEATHER_D = (110, 80, 55, 255)     # 皮革暗部

# 画斜着的木柄（从左下到右上）
for i in range(4, 14):  # 从x=4到x=13
    y = 14 - i + 2  # 计算对应的y
    draw.point((i, y), fill=WOOD_MID)
    draw.point((i+1, y), fill=WOOD_DARK)

# 顶部皮革包裹（在右上端）
for i in range(11, 14):
    y = 14 - i + 2
    draw.point((i, y), fill=LEATHER)
    draw.point((i+1, y), fill=LEATHER_D)

# 底部尖端
draw.point((4, 12), fill=WOOD_DARK)

# 保存为PNG
img.save(OUTPUT_FILE)
print(f"纹理已生成：{OUTPUT_FILE}")