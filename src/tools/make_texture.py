from PIL import Image

# 更沉稳的木色/皮革色（降低亮度，缩小色差）
WOOD_EDGE = (100, 65, 35, 255)
WOOD_CORE = (130, 90, 55, 255)
LEATHER_EDGE = (120, 55, 30, 255)   # 皮革外层
LEATHER_CORE = (150, 75, 45, 255)   # 皮革内层/高光

img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
pixels = img.load()

# 缩短长度，从 x=2 到 x=13（比之前短一点，显得更粗）
start_x = 2
end_x = 13
leather_start_x = 11  # 皮革包裹区间

for x in range(16):
    for y in range(16):
        s = x + y
        if start_x <= x <= end_x and 14 <= s <= 17: # 4像素宽
            
            # 圆头 (左下)
            if x == start_x and y >= 14:
                continue

            # 尖头 (右上，皮革区)，强制填充为皮革内层，饱满不缺失
            if x == end_x:
                pixels[x, y] = LEATHER_CORE if (s == 15 or s == 16) else LEATHER_EDGE
                continue

            # 常规部分上色（细腻的硬边渐变）
            if x >= leather_start_x:
                if s == 14 or s == 17:
                    pixels[x, y] = LEATHER_EDGE
                else:
                    pixels[x, y] = LEATHER_CORE
            else:
                if s == 14 or s == 17:
                    pixels[x, y] = WOOD_EDGE
                else:
                    pixels[x, y] = WOOD_CORE

img.save('wooden_handle.png')
print("✅ 木柄已优化：色调更沉稳，皮革包裹更细腻。")