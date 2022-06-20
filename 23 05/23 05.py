from PIL import Image, ImageDraw


def board(num, size):
    img = Image.new("RGB", (num * size, num * size), "white")
    draw = ImageDraw.Draw(img)
    counter = 0
    for x in range(0, num * size, size):
        for y in range(0, num * size, size):
            if counter % 2 == 0:  # черные клетки
                draw.rectangle((x, y, x + size, y + size), fill="black")
            else:
                draw.rectangle((x, y, x + size, y + size), fill="white")
            counter += 1
        counter -= 1 if num % 2 == 0 else 0

    img.save("res.png")