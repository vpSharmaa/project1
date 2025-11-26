from PIL import Image, ImageDraw

# Create blank square image
img = Image.new("RGBA", (512, 512), (30, 144, 255, 255))  # blue background
draw = ImageDraw.Draw(img)

# Draw calculator body
draw.rectangle((100, 80, 412, 380), fill="white", outline="black", width=8)

# Buttons (4x4 grid)
btn_size = 60
gap = 20
start_x = 130
start_y = 120

for row in range(4):
    for col in range(4):
        x1 = start_x + col * (btn_size + gap)
        y1 = start_y + row * (btn_size + gap)
        x2 = x1 + btn_size
        y2 = y1 + btn_size
        draw.rectangle((x1, y1, x2, y2), fill=(200, 200, 200),
                       outline="black", width=4)

# Speaker icon
draw.polygon([(200, 420), (240, 420), (260, 450),
              (240, 480), (200, 480)], fill="white")
draw.arc((260, 420, 330, 480), start=300, end=60,
         fill="white", width=8)

# Save ICO
img.save("talking_calculator.ico",
         format="ICO",
         sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])

print("Icon saved as talking_calculator.ico")
