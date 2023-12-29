import tkinter as tk
from tkinter import Canvas

# Función para aplicar la regla del autómata celular
def apply_rule(rule, neighborhood):
    binary_rule = format(rule, '08b')
    return int(binary_rule[7 - int(neighborhood, 2)], 2)

# Función para generar la siguiente generación del autómata
def generate_next_generation(cells, rule):
    new_cells = [0] * len(cells)
    for i in range(1, len(cells) - 1):
        neighborhood = ''.join(map(str, cells[i-1:i+2]))
        new_cells[i] = apply_rule(rule, neighborhood)
    return new_cells

# Función para actualizar el canvas con la nueva generación
def update_canvas():
    global cells, rule, canvas
    cells = generate_next_generation(cells, rule)
    draw_generation()
    root.after(100, update_canvas)

# Función para dibujar la generación en el canvas
def draw_generation():
    global cells, canvas
    canvas.delete("all")
    for i, cell in enumerate(cells):
        color = "black" if cell == 1 else "white"
        canvas.create_rectangle(i * cell_size, 0, (i + 1) * cell_size, cell_size, fill=color)

# Función para manejar el cambio en la selección de reglas
def rule_selection_changed():
    global rule_var
    rule = "".join(str(rule_var[i].get()) for i in range(8))
    rule = int(rule, 2)
    update_rule(rule)

# Función para actualizar la regla del autómata
def update_rule(new_rule):
    global rule, cells
    rule = new_rule
    cells = [0] * len(cells)
    cells[len(cells) // 2] = 1
    draw_generation()

# Configuración inicial
cell_size = 5
num_cells = 550 // cell_size
cells = [0] * num_cells
rule = 150  # Puedes cambiar esto según la regla inicial que desees
cells[num_cells // 2] = 1  # Célula inicial activa en el centro

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Automata Celular")

# Canvas para dibujar las generaciones
canvas = Canvas(root, width=550, height=400)
canvas.pack()

# Configurar las casillas seleccionables
rule_var = [tk.IntVar() for _ in range(8)]
checkboxes = []
for i in range(8):
    checkbox = tk.Checkbutton(root, text="Casilla seleccionable-" + format(i, '03b'),
                               variable=rule_var[i], command=rule_selection_changed)
    checkbox.pack(side=tk.LEFT)
    checkboxes.append(checkbox)

# Iniciar el programa
update_canvas()
root.mainloop()