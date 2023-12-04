from drawbot_skia.drawbot import oval, rect, newPage, saveImage, stroke, fill, strokeWidth

# зададим правила для выбора
rules = [1, 0, 1, 0, 2, 0, 1, "гусь"] * 20

# создадим новую страницу
w, h = 742.5, 1050
newPage(w, h)

margin = 80
x = margin
y = h - margin
step = (w - margin * 2) / 6
size = step

fill (None)
stroke(0, 0, 0)  # черный цвет контура
strokeWidth (3)

for rule in rules:
    # контурный круг, если правило == 2
    if rule == 2:
        oval(x, y - step, size, size)
    # круг, если правило == 0
    elif rule == 0:
        rect(x, y - step, size, size)
    # квадрат, если правило == 1
    elif rule == 1:
        oval(x, y - step, size, size)
    # всё другое print в консоль
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

saveImage("summary_2_example.pdf")
