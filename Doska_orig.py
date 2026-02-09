import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import subprocess

class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Инструмент анализа данных")
        self.root.geometry("1920x1080")

        # Основная рамка
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Холст для рисования и графов
        self.canvas = tk.Canvas(self.main_frame, bg='white')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Панель инструментов
        self.tool_frame = ttk.Frame(self.main_frame, width=220)
        self.tool_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)
        self.tool_frame.pack_propagate(False)

        # Стиль и состояние
        self.mode = 'draw'  # 'draw', 'arrow', 'line_straight', 'add_image', 'add_node', 'connect', 'move', 'delete'
        self.current_color = 'black'
        self.actions = []  # список для отмены
        self.images = []   # список (canvas_image_id, PIL_image, tk_image)
        self.nodes = {}    # id: {'label':..., 'x':..., 'y':...}
        self.edges = []    # {'from':..., 'to':..., 'id':...}
        self.node_counter = 0
        self.drag_data = {"item": None, "x": 0, "y": 0}
        self.current_straight_line = None
        self.straight_line_start = (0, 0)
        self.connect_start_node = None

        # Создаем кнопки
        self.create_widgets()

        # Обработка событий
        self.canvas.bind('<ButtonPress-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_move_press)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

        # Обработка перетаскивания изображений
        self.canvas.tag_bind('draggable', '<ButtonPress-1>', self.start_move_image)
        self.canvas.tag_bind('draggable', '<B1-Motion>', self.move_image)

        self.process = subprocess.Popen("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)

    def create_widgets(self):
        # Цвета
        ttk.Label(self.tool_frame, text="Цвета:").pack(pady=5)
        colors = [
            ('Красный', 'red'),
            ('Желтый', 'yellow'),
            ('Зеленый', 'green'),
            ('Черный', 'black'),
            ('Синий', 'blue'),
            ('Серый', 'gray')
        ]
        for name, color in colors:
            btn = ttk.Button(self.tool_frame, text=name, command=lambda c=color: self.set_color(c))
            btn.pack(fill=tk.X, padx=10, pady=2)

        ttk.Separator(self.tool_frame, orient='horizontal').pack(fill=tk.X, pady=10)

        # Режимы
        ttk.Label(self.tool_frame, text="Режимы:").pack(pady=5)
        ttk.Button(self.tool_frame, text='Рисовать', command=self.set_draw_mode).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Стрелка', command=self.set_arrow_mode).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Ровная линия', command=self.set_line_straight_mode).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Добавить изображение', command=self.load_image).pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(self.tool_frame, text='Добавить объект', command=self.add_node).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Соединить объекты', command=self.set_connect_mode).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Перемещать', command=self.set_move_mode).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Удалить', command=self.set_delete_mode).pack(fill=tk.X, padx=10, pady=2)
        ttk.Separator(self.tool_frame, orient='horizontal').pack(fill=tk.X, pady=10)
        # Вспомогательные
        ttk.Button(self.tool_frame, text='Отменить', command=self.undo_last_action).pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(self.tool_frame, text='Импорт', command=self.import_data).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.tool_frame, text='Экспорт', command=self.export_data).pack(fill=tk.X, padx=10, pady=2)

        # Изначальный режим
        self.set_draw_mode()

    # --- Установка режимов ---
    def set_draw_mode(self):
        self.mode = 'draw'

    def set_arrow_mode(self):
        self.mode = 'arrow'

    def set_line_straight_mode(self):
        self.mode = 'line_straight'
        self.current_straight_line = None

    def set_add_image_mode(self):
        self.mode = 'add_image'

    def set_add_node_mode(self):
        self.mode = 'add_node'

    def set_connect_mode(self):
        self.mode = 'connect'
        self.connect_start_node = None

    def set_move_mode(self):
        self.mode = 'move'

    def set_delete_mode(self):
        self.mode = 'delete'

    # --- Цвет ---
    def set_color(self, color):
        self.current_color = color


    # --- Добавление изображений ---
    def load_image(self):
        filename = filedialog.askopenfilename(
            title='Выберите PNG или JPG',
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if filename:
            try:
                pil_img = Image.open(filename)
                tk_img = ImageTk.PhotoImage(pil_img)
                # Вставляем изображение
                image_id = self.canvas.create_image(50, 50, image=tk_img, anchor='nw', tags=('draggable',))
                self.images.append((image_id, pil_img, tk_img))
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

    # --- Добавление объектов (узлов) ---
    def add_node(self):
        label = simpledialog.askstring("?", "Введите название объекта:")
        if label:
            x, y = 100 + self.node_counter * 20, 100 + self.node_counter * 20
            node_id = self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='lightblue', outline='blue', width=2)
            text_id = self.canvas.create_text(x, y, text=label)
            self.nodes[node_id] = {'label': label, 'x': x, 'y': y}
            self.node_counter += 1
            # Связываем события
            self.canvas.tag_bind(node_id, '<Button-1>', lambda e, id=node_id: self.on_node_click(e, id))
            self.canvas.tag_bind(text_id, '<Button-1>', lambda e, id=node_id: self.on_node_click(e, id))
            self.canvas.tag_bind(node_id, '<B1-Motion>', lambda e, id=node_id: self.move_node(e, id))
            self.canvas.tag_bind(text_id, '<B1-Motion>', lambda e, id=node_id: self.move_node(e, id))

    def on_node_click(self, event, node_id):
        if self.mode == 'connect':
            if self.connect_start_node is None:
                self.connect_start_node = node_id
            else:
                # Создать линию
                start_x, start_y = self.nodes[self.connect_start_node]['x'], self.nodes[self.connect_start_node]['y']
                end_x, end_y = self.nodes[node_id]['x'], self.nodes[node_id]['y']
                line_id = self.canvas.create_line(start_x, start_y, end_x, end_y, fill='gray', width=2)
                self.edges.append({'from': self.connect_start_node, 'to': node_id, 'id': line_id})
                self.connect_start_node = None
        elif self.mode == 'delete':
            self.delete_node(node_id)

    def move_node(self, event, node_id):
        dx = event.x - self.nodes[node_id]['x']
        dy = event.y - self.nodes[node_id]['y']
        self.canvas.move(node_id, dx, dy)
        # Обновляем позицию узла
        self.nodes[node_id]['x'] += dx
        self.nodes[node_id]['y'] += dy
        # Обновляем связанный текст
        for item in self.canvas.find_withtag('current'):
            if self.canvas.type(item) == 'text':
                self.canvas.move(item, dx, dy)
        # Обновляем линии
        for edge in self.edges:
            if edge['from'] == node_id or edge['to'] == node_id:
                start_node = self.nodes[edge['from']]
                end_node = self.nodes[edge['to']]
                self.canvas.coords(edge['id'], start_node['x'], start_node['y'], end_node['x'], end_node['y'])

    def delete_node(self, node_id):
        self.canvas.delete(node_id)
        # Удаляем связанный текст
        for item in self.canvas.find_withtag('current'):
            if self.canvas.type(item) == 'text':
                self.canvas.delete(item)
        # Удаляем связи
        to_delete = [edge for edge in self.edges if edge['from'] == node_id or edge['to'] == node_id]
        for edge in to_delete:
            self.canvas.delete(edge['id'])
            self.edges.remove(edge)
        # Удаляем из nodes
        if node_id in self.nodes:
            del self.nodes[node_id]

    # --- Обработка нажатий и перетаскиваний ---
    def on_button_press(self, event):
        if self.mode == 'draw':
            line_id = self.canvas.create_line(event.x, event.y, event.x, event.y, fill=self.current_color, width=2)
            self.actions.append([line_id])
            self.last_x, self.last_y = event.x, event.y
        elif self.mode == 'arrow':
            arrow_id = self.canvas.create_line(event.x, event.y, event.x, event.y, fill=self.current_color, width=2, arrow='last')
            self.actions.append([arrow_id])
            self.last_x, self.last_y = event.x, event.y
        elif self.mode == 'line_straight':
            self.straight_line_start = (event.x, event.y)
            self.current_straight_line = self.canvas.create_line(event.x, event.y, event.x, event.y, fill=self.current_color, width=2)
            self.actions.append([self.current_straight_line])
        elif self.mode == 'add_image':
            # Возможна реализация добавления изображений по клику
            pass
        elif self.mode == 'add_node':
            self.add_node()
        elif self.mode == 'connect':
            # Обработка через on_node_click
            pass
        elif self.mode == 'move':
            # Обработка через bind
            pass
        elif self.mode == 'delete':
            # Обработка через on_node_click
            pass

    def on_move_press(self, event):
        if self.mode in ['draw', 'arrow']:
            if self.actions:
                line_id = self.actions[-1][0]
                self.canvas.coords(line_id, self.last_x, self.last_y, event.x, event.y)
        elif self.mode == 'line_straight' and self.current_straight_line:
            x0, y0 = self.straight_line_start
            delta_x = abs(event.x - x0)
            delta_y = abs(event.y - y0)
            if delta_x > delta_y:
                end_x, end_y = event.x, y0
            else:
                end_x, end_y = x0, event.y
            self.canvas.coords(self.current_straight_line, x0, y0, end_x, end_y)

    def on_button_release(self, event):
        if self.mode in ['draw', 'arrow']:
            self.actions.append([self.canvas.find_withtag('current')[0]])
        elif self.mode == 'line_straight':
            self.actions.append([self.current_straight_line])
            self.current_straight_line = None

    # --- Отмена последнего действия ---
    def undo_last_action(self):
        if self.actions:
            last_action = self.actions.pop()
            for item_id in last_action:
                self.canvas.delete(item_id)

    # --- Импорт / Экспорт ---
    def import_data(self):
        filename = filedialog.askopenfilename(title='Импорт данных', filetypes=[('JSON', '*.json')])
        if filename:
            # Реализовать загрузку данных графа или рисунков
            messagebox.showinfo("Информация", "Функция импорта еще не реализована.")

    def export_data(self):
        filename = filedialog.asksaveasfilename(title='Экспорт данных', defaultextension='.json', filetypes=[('JSON', '*.json')])
        if filename:
            # Реализовать сохранение
            messagebox.showinfo("Информация", "Функция экспорта еще не реализована.")

    # --- Перетаскивание изображений ---
    def start_move_image(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]
        if 'draggable' in self.canvas.gettags(item):
            self.drag_data["item"] = item
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y


    def move_image(self, event):
        item = self.drag_data["item"]
        if item:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            self.canvas.move(item, dx, dy)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y



# запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()