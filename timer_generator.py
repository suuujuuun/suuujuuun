from datetime import datetime
from PIL import Image, ImageDraw

start = datetime(2025, 7, 4)
end = datetime(2026, 1, 4)
now = datetime.utcnow()

total = (end - start).total_seconds()
elapsed = (now - start).total_seconds()
progress = max(0, min(elapsed / total, 1))

size = 300
img = Image.new("RGB", (size, size), "white")
draw = ImageDraw.Draw(img)
draw.ellipse((0, 0, size, size), outline="lightgray", width=20)

end_angle = 360 * progress
draw.pieslice((0, 0, size, size), start=270, end=270 + end_angle, outline="blue", width=20)

img.save("countdown.png")
