import tkinter as tk
import math

class Polygon:
    def __init__(self, canvas, x1, y1, x2, y2, x3, y3, color='black'):
        self.canvas = canvas
        self.polygon = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
        self.scale_factor = 1
        self.rotation_center_x = 0
        self.rotation_center_y = 0

    def set_scale_factor(self, scale_factor):
        self.scale_factor = scale_factor
        self.update_polygon()

    def set_rotation_center(self, x, y):
        self.rotation_center_x = x
        self.rotation_center_y = y
        self.update_polygon()

    def rotate(self, angle):
        self.update_polygon(rotation=angle)

    def update_polygon(self, scale=None, rotation=None):
        if scale is not None:
            scale_transform = tk.ScaleTransform(scale=self.scale_factor)
            points = [(scale_transform.transform((x, y)),) for x, y in self.get_points()]
        else:
            points = [(x, y) for x, y in self.get_points()]

        if rotation is not None:
            rotation_matrix = [
                [math.cos(rotation), -math.sin(rotation)],
                [math.sin(rotation), math.cos(rotation)]
            ]
            rotation_transform = tk.Transform(translation=(
                -self.rotation_center_x,
                -self.rotation_center_y
            )) + tk.Transform(matrix=rotation_matrix)
            points = [(rotation_transform.transform(point),) for point in points]

        self.canvas.coords(self.polygon, *points)

    
    def get_points(self):
        return [(0, 0), (100, 0), (50, 100)]

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

polygon = Polygon(canvas, 0, 0, 100, 0, 50, 100)

scale = tk.Scale(root, from_=0.1, to=2, command=lambda x: polygon.set_scale_factor(float(x)))
scale.pack()

rotation_center_x = tk.Scale(root, from_=-100, to=100, command=lambda x: polygon.set_rotation_center(float(x), 0))
rotation_center_y = tk.Scale(root, from_=-100, to=100, command=lambda x: polygon.set_rotation_center(0, float(x)))
rotation_center_x.pack()
rotation_center_y.pack()

rotate_button = tk.Button(root, text="Rotate", command=lambda: polygon.rotate(math.radians(45)))
rotate_button.pack()

root.mainloop()
