from PIL import Image
import os
i = 0

for dr in os.listdir("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"):
    k = os.listdir("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"+dr+"//")
    i = 0
    while i < len(k):
        
        img = Image.open("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"+dr+"//"+k[i])
        width = 500
        height = 506
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save("C://Users//User//Desktop//Natsulogue//game//mod_assets//natsuki//sitting//"+dr+"//"+k[i])
        i += 1
