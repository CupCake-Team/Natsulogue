from PIL import Image, ImageEnhance
import os
i = 0

for dr in os.listdir("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"):
    k = os.listdir("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"+dr+"//")
    i = 0
    while i < len(k):
        
        img = Image.open("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"+dr+"//"+k[i])
        width = 597
        rate = (width / float(img.size[0]))
        height = int((float(img.size[1])*float(rate)))
        #height = 605
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        enhancer = ImageEnhance.Contrast(resized_img)
        
        level = 1.1
        s_image = enhancer.enhance(level)
        sharpness = ImageEnhance.Sharpness(s_image)
        n_image = sharpness.enhance(level+0.1)
        n_image.save("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"+dr+"//"+k[i])
        i += 1
