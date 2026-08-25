from PIL import Image

# 高对比度颜色设置（保留前次设置的硬边）
WOOD_EDGE = (110, 70, 30, 255)      # 木柄边缘：深木色
WOOD_CORE = (180, 120, 60, 255)     # 木柄核心：亮木色
LEATHER_EDGE = (130, 60, 20, 255)   # 皮革边缘：深红棕
LEATHER_CORE = (200, 100, 50, 255)  # 皮革核心：亮红棕

# 创建 16x16 透明图片
img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
pixels = img.load()

# 尺寸参数
start_x = 2
end_x = 13
leather_start_x = 11  # 80%处开始包皮革

for x in range(16):
    for y in range(16):
        # 判断对角线位置（宽度3像素）
        s = x + y
        if start_x <= x <= end_x and 15 <= s <= 17:
            
            # 完美圆头逻辑：移除左下角最底部的两个点 (2,14) 和 (2,15)，只保留 (2,13)
            if x == start_x and y >= 14:
                continue
            
            # 判定皮革区域 (右上角)
            if x >= leather_start_x:
                if s == 15 or s == 17:
                    color = LEATHER_EDGE
                else:
                    color = LEATHER_CORE
            else:
                # 木柄主体（高对比度硬边）
                if s == 15 or s == 17:
                    color = WOOD_EDGE
                else:
                    color = WOOD_CORE

            pixels[x, y] = color

# 保存文件
img.save('wooden_handle.png')
print("✅ 木柄纹理已修复：圆头完整，无冗余像素。")