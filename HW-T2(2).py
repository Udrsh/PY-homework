from drawbot_skia.drawbot import oval, rect, newPage, saveImage, stroke, fill, strokeWidth


rules = [1, 0, 1, 0, 2, 0, 1, "гусь"] * 20


w, h = 742.5, 1050
newPage(w, h)

margin = 80
x = margin
y = h - margin
step = (w - margin * 2) / 6
size = step

for rule in rules:
    
    if rule == 2:
        fill(1, 1, 0)  
        stroke(1, 0, 0)  
        oval(x, y - step, size, size)
   
    elif rule == 0:
        fill(1, 0, 0)  
        stroke(1, 1, 1)  
        rect(x, y - step, size, size)
   
    elif rule == 1:
        fill(0, 1, 0)  
        stroke(0, 0, 0)  
        oval(x, y - step, size, size)
    
    else:
        print(rule, "<— неизвестное правило")

    x += step

    if x >= w - margin:
        x = margin
        y -= step

    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin

saveImage("T2(2).pdf")
