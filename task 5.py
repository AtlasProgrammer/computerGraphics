import tkinter as tk
from tkinter import filedialog
from PIL import Image

class ImageAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Analyzer")
        self.image = None
        self.table_data = []

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.start_x_label = tk.Label(root, text="Start X:")
        self.start_x_label.pack()
        self.start_x_entry = tk.Entry(root, width=5)
        self.start_x_entry.insert(tk.END, "0")
        self.start_x_entry.pack()

        self.end_x_label = tk.Label(root, text="End X:")
        self.end_x_label.pack()
        self.end_x_entry = tk.Entry(root, width=5)
        self.end_x_entry.insert(tk.END, "10")
        self.end_x_entry.pack()

        self.start_y_label = tk.Label(root, text="Start Y:")
        self.start_y_label.pack()
        self.start_y_entry = tk.Entry(root, width=5)
        self.start_y_entry.insert(tk.END, "0")
        self.start_y_entry.pack()

        self.end_y_label = tk.Label(root, text="End Y:")
        self.end_y_label.pack()
        self.end_y_entry = tk.Entry(root, width=5)
        self.end_y_entry.insert(tk.END, "10")
        self.end_y_entry.pack()

        self.table = tk.Listbox(root, width=100, height=20)
        self.table.pack()

        self.change_button = tk.Button(root, text="Change Colors", command=self.change_colors)
        self.change_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path)
        self.update_table()

    def brightness(self, pixel):
        return sum(pixel) / 3

    def update_table(self):
        if self.image:
            start_x = int(self.start_x_entry.get())
            end_x = int(self.end_x_entry.get())
            start_y = int(self.start_y_entry.get())
            end_y = int(self.end_y_entry.get())
            self.table_data.clear()
            self.table.delete(0, tk.END)  # Очистка старой таблицы
            for y in range(start_y, min(end_y, self.image.height)):
                row = []
                for x in range(start_x, min(end_x, self.image.width)):
                    pixel = self.image.getpixel((x, y))
                    color = "#" + "".join(f"{c:02x}" for c in pixel)
                    brightness_val = self.brightness(pixel)
                    row.append(f"({color}, Brightness: {brightness_val:.2f}")
                self.table_data.append(row)
                self.table.insert(tk.END, " | ".join(row))

    def change_colors(self):
        if self.table_data:
            self.table.delete(0, tk.END)  # Очистка старой таблицы
            for item in self.table_data:
                new_items = []
                for color_info in item:
                    color_hex = color_info.split(",")[0].strip()[2:]
                    if len(color_hex) % 2 == 0:  # Проверка длины строки цвета
                        color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
                        new_color = tuple(255 - c for c in color)  # Замена цвета на противоположный
                        new_color_hex = "#" + "".join(f"{c:02x}" for c in new_color)
                        new_items.append(f"({new_color_hex}, Brightness: {self.brightness(new_color):.2f}")
                self.table.insert(tk.END, " | ".join(new_items))

root = tk.Tk()
image_analyzer = ImageAnalyzer(root)
root.mainloop()
