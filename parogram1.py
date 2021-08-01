import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width = 400, height = 300)
canvas.pack()


def leaperYear():
    year = int(entry.get())
    if year % 4 == 0 and year % 100 !=0:
        print('{} is leaper year'.format(year))
    else:
        print('{} is not leaper year'.format(year))


label = tk.Label(root, text = 'Input Year').place(x = 120, y= 100)
entry = tk.Entry(root)
canvas.create_window(250, 120, window = entry)
button = tk.Button(root, text = 'Click Me', command = leaperYear).place(x = 220, y = 150)

root.mainloop()
