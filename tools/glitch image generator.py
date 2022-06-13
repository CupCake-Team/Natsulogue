from PIL import Image
import random

w_i = Image.open("k.png")
(width, height) = w_i.size

pix = int(input("количество пикселей в линии "))

chance = int(input("шанс на удаление пикселя не больше 100 "))

pix_size = int(width / pix)

fw = 0
fh = 0

glitch = Image.new("RGBA", (width, height), (0,0,0,0))


while True:
    cord = (fw, fh, fw+pix_size, fh+pix_size)
    p = w_i.crop(cord)
    c = random.randint(1, 100)
    if c >= chance:
        glitch.paste(p, (fw, fh))
        fw += pix_size
    else:
        fw += pix_size

    if fw >= width:
        fw = 0
        fh += pix_size

    if fh >= height:
        break

glitch.save("glitch.png")
