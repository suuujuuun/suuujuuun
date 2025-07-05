from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

start = datetime(2025, 7, 2)
end = datetime(2026, 1, 2)
now = datetime.utcnow()

total = (end - start).total_seconds()
elapsed = (now - start).total_seconds()
progress = max(0, min(elapsed / total, 1))
percent = round(progress * 100, 1)  

size = 150
bg_color = "white"
circle_color = "#4A90E2"
trail_color = "#E0E0E0"
text_color = "#333333"

img = Image.new("RGB", (size, size), bg_color)
draw = ImageDraw.Draw(img)

margin = 10
draw.ellipse(
    (margin, margin, size - margin, size - margin),
    outline=trail_color,
    width=10,
)
end_angle = 360 * progress
draw.arc(
    (margin, margin, size - margin, size - margin),
    start=-90,
    end=-90 + end_angle,
    fill=circle_color,
    width=10,
)

font_size = 20
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", font_size)
except:
    font = ImageFont.load_default()

text = f"{percent}%"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

draw.text(
    ((size - text_width) / 2, (size - text_height) / 2),
    text,
    fill=text_color,
    font=font,
)

img.save("countdown.png")
