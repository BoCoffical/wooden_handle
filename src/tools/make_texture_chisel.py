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
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "main", "resources", "assets", "wooden_handle", "textures", "item", filename)

INPUT = find_texture("resonance_chisel.png")
OUTPUT = os.path.join(os.path.dirname(INPUT), "resonance_chisel_optimized.png")

# ---------- 亮度调整函数 ----------
def adjust_brightness(pixel):
    r, g, b, a = pixel
    # 仅处理灰色/铁质像素（R≈G≈B）
    if abs(r - g) < 15 and abs(g - b) < 15:
        # 亮度 = 通道平均值
        lum = (r + g + b) // 3
        # 分段映射：
        # 0~50 映射到 60~90  (暗部提亮)
        # 50~120 映射到 90~190 (中间调大幅提亮)
        # 120~255 映射到 190~255 (高光微调，保持明亮)
        if lum < 50:
            new_lum = int(60 + (lum / 50) * 30)     # 60~90
        elif lum < 120:
            new_lum = int(90 + ((lum - 50) / 70) * 100)  # 90~190
        else:
            new_lum = int(190 + ((lum - 120) / 135) * 65) # 190~255
        # 确保新亮度不超过255
        new_lum = min(255, max(0, new_lum))
        return (new_lum, new_lum, new_lum, a)
    return pixel

# ---------- 读取与处理 ----------
img = Image.open(INPUT).convert("RGBA")
data = img.getdata()
new_data = [adjust_brightness(p) for p in data]
new_img = Image.new("RGBA", img.size)
new_img.putdata(new_data)
new_img.save(OUTPUT)
print(f"共鸣凿纹理优化完成，输出：{OUTPUT}")