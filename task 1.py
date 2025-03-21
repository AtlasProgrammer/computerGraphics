import tkinter as tk
import math

shapes = []

def draw_line():
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    shapes.append(canvas.create_line(x1, y1, x2, y2, fill="blue"))

def draw_ellipse():
    x = int(entry_x.get())
    y = int(entry_y.get())
    radius_x = int(entry_radius_x.get())
    radius_y = int(entry_radius_y.get())
    shapes.append(canvas.create_oval(x-radius_x, y-radius_y, x+radius_x, y+radius_y, fill="blue"))

def draw_polygon():
    x = int(entry_x.get())
    y = int(entry_y.get())
    sides = int(entry_sides.get())
    size = int(entry_size.get())
    thickness = int(entry_thickness.get())
    angle = 360 / sides
    points = []
    for i in range(sides):
        x_point = x + size * math.cos(math.radians(angle*i))
        y_point = y + size * math.sin(math.radians(angle*i))
        points.extend([x_point, y_point])
    shapes.append(canvas.create_polygon(points, fill="blue", outline="blue", width=thickness))

def draw_random_polygon():
    x = int(entry_x.get())
    y = int(entry_y.get())
    sides = int(entry_sides.get())
    size = int(entry_size.get())
    thickness = int(entry_thickness.get())
    angle = 360 / sides
    radius = size / (2 * math.sin(math.pi / sides))
    points = []
    for i in range(sides):
        x_point = x + radius * math.cos(math.radians(angle*i))
        y_point = y + radius * math.sin(math.radians(angle*i))
        points.extend([x_point, y_point])
    shapes.append(canvas.create_polygon(points, fill="blue", outline="blue", width=thickness))

def draw_polygon_from_coords():
    coords_str = entry_coords.get()
    coords = [tuple(map(int, coord.split(','))) for coord in coords_str.split()]
    shapes.append(canvas.create_polygon(coords, fill="blue", outline="blue"))

def delete_shape():
    if shapes:
        canvas.delete(shapes.pop())

def clear_shapes():
    for shape in shapes:
        canvas.delete(shape)
    shapes.clear()

# Создаем графический интерфейс
root = tk.Tk()
root.title("Рисование фигур")
root.geometry("1000x600")

# Создаем элементы для ввода данных
frame = tk.Frame(root)
frame.pack(side=tk.LEFT)

label_x1 = tk.Label(frame, text="Начальная координата для линии X:")
label_x1.pack()
entry_x1 = tk.Entry(frame)
entry_x1.pack()

label_y1 = tk.Label(frame, text="Начальная координата для линии Y:")
label_y1.pack()
entry_y1 = tk.Entry(frame)
entry_y1.pack()

label_x2 = tk.Label(frame, text="Конечная координата для линии X:")
label_x2.pack()
entry_x2 = tk.Entry(frame)
entry_x2.pack()

label_y2 = tk.Label(frame, text="Конечная координата для линии Y:")
label_y2.pack()
entry_y2 = tk.Entry(frame)
entry_y2.pack()

button_draw_line = tk.Button(frame, text="Рисуем линию", command=draw_line)
button_draw_line.pack()

label_x = tk.Label(frame, text="X координата:")
label_x.pack()
entry_x = tk.Entry(frame)
entry_x.pack()

label_y = tk.Label(frame, text="Y координата:")
label_y.pack()
entry_y = tk.Entry(frame)
entry_y.pack()

label_radius_x = tk.Label(frame, text="X радиус:")
label_radius_x.pack()
entry_radius_x = tk.Entry(frame)
entry_radius_x.pack()

label_radius_y = tk.Label(frame, text="Y радиус:")
label_radius_y.pack()
entry_radius_y = tk.Entry(frame)
entry_radius_y.pack()

button_draw_ellipse = tk.Button(frame, text="Рисуем эллипс", command=draw_ellipse)
button_draw_ellipse.pack()

label_sides = tk.Label(frame, text="Количество сторон:")
label_sides.pack()
entry_sides = tk.Entry(frame)
entry_sides.pack()

label_size = tk.Label(frame, text="Радиус описанной окружности:")
label_size.pack()
entry_size = tk.Entry(frame)
entry_size.pack()

label_thickness = tk.Label(frame, text="Толщина границы:")
label_thickness.pack()
entry_thickness = tk.Entry(frame)
entry_thickness.pack()

button_draw_polygon = tk.Button(frame, text="Рисуем полигон", command=draw_polygon)
button_draw_polygon.pack()

button_draw_random_polygon = tk.Button(frame, text="Рисуем случайный полигон", command=draw_random_polygon)
button_draw_random_polygon.pack()

label_coords = tk.Label(frame, text="Координаты:")
label_coords.pack()
entry_coords = tk.Entry(frame)
entry_coords.pack()

button_draw_polygon_from_coords = tk.Button(frame, text="Рисуем полигон из координат", command=draw_polygon_from_coords)
button_draw_polygon_from_coords.pack()

button_delete_shape = tk.Button(frame, text="Удалить фигуру", command=delete_shape)
button_delete_shape.pack()

button_clear_shapes = tk.Button(frame, text="Очистить все фигуры", command=clear_shapes)
button_clear_shapes.pack()

# Создаем холст для рисования
canvas = tk.Canvas(root, bg="white", width=600, height=600)
canvas.pack(side=tk.RIGHT)

root.mainloop()
