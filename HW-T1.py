from drawbot_skia.drawbot import rect, oval, saveImage

step = 150

#############
# задание 1 #
#############


y = 150
for i in range(5):
    rect(150, y, 150, 100) 
    y = y + step

saveImage("T1.pdf")

#############
# задание 2 #
#############


y = 150
x = 150
for i in range(5):
    for j in range(5):
        if (j % 2 == 0):
            rect(x, y, 150, 100) 
        else:
            oval(x, y, 100, 100)
            
        x = x + 150
    
    x = step
    y = y + step

saveImage("T2.pdf")
