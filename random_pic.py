from PIL import Image
from random import randint

img = Image. new('RGB', (400,400), color = (255, 255, 255))
img. save('ran_img.png')

w = img.size[0]

parx,pary =0,0

for x in range(0,(w*w)//64):
    ran_R = randint(0,255)
    ran_G = randint(0,255)
    ran_B = randint(0,255)

    #wb = randint(0,1)

    #if(wb == 1):
    #    ran_R,ran_G,ran_B = 0,0,0
    #else:
    #    ran_R,ran_G,ran_B = 255,255,255
    

    pixel = (ran_R,ran_G,ran_B)
    #print(parx,pary)
    
    img.putpixel((parx,pary),pixel)
    img.putpixel((parx+1,pary),pixel)
    img.putpixel((parx+2,pary),pixel)
    img.putpixel((parx+3,pary),pixel)
    img.putpixel((parx+4,pary),pixel)
    img.putpixel((parx+5,pary),pixel)
    img.putpixel((parx+6,pary),pixel)
    img.putpixel((parx+7,pary),pixel)

    img.putpixel((parx,pary+1),pixel)
    img.putpixel((parx+1,pary+1),pixel)
    img.putpixel((parx+2,pary+1),pixel)
    img.putpixel((parx+3,pary+1),pixel)
    img.putpixel((parx+4,pary+1),pixel)
    img.putpixel((parx+5,pary+1),pixel)
    img.putpixel((parx+6,pary+1),pixel)
    img.putpixel((parx+7,pary+1),pixel)

    img.putpixel((parx,pary+2),pixel)
    img.putpixel((parx+1,pary+2),pixel)
    img.putpixel((parx+2,pary+2),pixel)
    img.putpixel((parx+3,pary+2),pixel)
    img.putpixel((parx+4,pary+2),pixel)
    img.putpixel((parx+5,pary+2),pixel)
    img.putpixel((parx+6,pary+2),pixel)
    img.putpixel((parx+7,pary+2),pixel)


    img.putpixel((parx,pary+3),pixel)
    img.putpixel((parx+1,pary+3),pixel)
    img.putpixel((parx+2,pary+3),pixel)
    img.putpixel((parx+3,pary+3),pixel)
    img.putpixel((parx+4,pary+3),pixel)
    img.putpixel((parx+5,pary+3),pixel)
    img.putpixel((parx+6,pary+3),pixel)
    img.putpixel((parx+7,pary+3),pixel)

    img.putpixel((parx,pary+4),pixel)
    img.putpixel((parx+1,pary+4),pixel)
    img.putpixel((parx+2,pary+4),pixel)
    img.putpixel((parx+3,pary+4),pixel)
    img.putpixel((parx+4,pary+4),pixel)
    img.putpixel((parx+5,pary+4),pixel)
    img.putpixel((parx+6,pary+4),pixel)
    img.putpixel((parx+7,pary+4),pixel)

    img.putpixel((parx,pary+5),pixel)
    img.putpixel((parx+1,pary+5),pixel)
    img.putpixel((parx+2,pary+5),pixel)
    img.putpixel((parx+3,pary+5),pixel)
    img.putpixel((parx+4,pary+5),pixel)
    img.putpixel((parx+5,pary+5),pixel)
    img.putpixel((parx+6,pary+5),pixel)
    img.putpixel((parx+7,pary+5),pixel)

    img.putpixel((parx,pary+6),pixel)
    img.putpixel((parx+1,pary+6),pixel)
    img.putpixel((parx+2,pary+6),pixel)
    img.putpixel((parx+3,pary+6),pixel)
    img.putpixel((parx+4,pary+6),pixel)
    img.putpixel((parx+5,pary+6),pixel)
    img.putpixel((parx+6,pary+6),pixel)
    img.putpixel((parx+7,pary+6),pixel)

    img.putpixel((parx,pary+7),pixel)
    img.putpixel((parx+1,pary+7),pixel)
    img.putpixel((parx+2,pary+7),pixel)
    img.putpixel((parx+3,pary+7),pixel)
    img.putpixel((parx+4,pary+7),pixel)
    img.putpixel((parx+5,pary+7),pixel)
    img.putpixel((parx+6,pary+7),pixel)
    img.putpixel((parx+7,pary+7),pixel)


    if(parx == w-8):
        parx = 0
        pary = pary + 8
    else:
        parx = parx + 8
    
img. save('ran_img.png')
print("Your Random Pic is generated")
