from PIL import Image, ImageDraw


class SetColorTheme:

    def __init__(self, name: str):
        self.name = name
        self.__img = Image.open(f"{self.name}.png")
        self.__pix = self.__img.load()
        self.__width = self.__img.width
        self.__height = self.__img.height
        self.__draw = ImageDraw.Draw(self.__img)
        self.__notTransparency = 170

    def red(self):
        self.__convert(-200,50,  50)
        self.__save()
        return

    def blue(self):
        self.__convert(1000, -30, -1000)
        self.__save()
        return

    def green(self):
        self.__convert(200, -100, 0)
        self.__save()
        return

    def purple(self):
        self.__convert(-100, 30, -100)
        self.__save()
        return
    
    def yellow(self):
        self.__convert(-500,-100, 1000)
        self.__save()
        return

    def gray(self):
        for x in range(self.__width):
            for y in range(self.__height):
                r = self.__pix[x, y][0]
                g = self.__pix[x, y][1]
                b = self.__pix[x, y][2]
                sr = (r + g + b) // 3
                self.__draw.point((x, y), (255 - sr, 255 - sr, 255 - sr))
        self.__save()
        return        

    def __convert(self, a: int, b: int, c:int):
        for x in range(self.__width):
            for y in range(self.__height):
                r = self.__pix[x, y][0]
                g = self.__pix[x, y][1]
                b2 = self.__pix[x, y][2]
                self.__draw.point((x, y), (255 - r - a, 255 - g - b, 255 - b2 - c))

    def __save(self):
        self.__img.putalpha(self.__notTransparency)    
        self.__img.show()    
        self.__img.save(f"{self.name}_new.png", "PNG")    
        return

SetColorTheme("textbox").blue()
SetColorTheme("namebox").blue()


