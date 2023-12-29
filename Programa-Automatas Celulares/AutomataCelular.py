import tkinter as tk
from PIL import Image, ImageTk

class AutomataCelular:
    def __init__(self, width, height, rule):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
        self.rule = rule
        self.current_generation = [0] * width
        self.current_generation[width // 2] = 1

    def procesar_generacion(self):
        new_generation = [0] * self.width
        for i in range(1, self.width - 1):
            neighborhood = ''.join(map(str, self.current_generation[i-1:i+2]))
            new_generation[i] = self.apply_rule(self.rule, neighborhood)

        self.grid.append(new_generation)
        self.current_generation = new_generation

    @staticmethod
    def apply_rule(rule, neighborhood):
        binary_rule = format(rule, '08b')
        return int(binary_rule[7 - int(neighborhood, 2)], 2)

class InterfazGrafica:
    def __init__(self, root, automata):
        self.root = root
        self.automata = automata

        # Inicializar la interfaz gráfica
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        # Configurar la ventana principal
        self.root.title("Automata Celular")

        # Cuadricula para mostrar el automata celular
        self.canvas = tk.Canvas(self.root, width=550, height=400, borderwidth=0, highlightthickness=0, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=10)

        # Botón para procesar la generación
        procesar_btn = tk.Button(self.root, text="Procesar", command=self.procesar)
        procesar_btn.grid(row=0, column=1)

        # Casillas seleccionables
        opciones = ["111", "110", "101", "100", "011", "010", "001", "000"]
        self.var_reglas = [tk.IntVar() for _ in range(len(opciones))]

        for i, opcion in enumerate(opciones):
            checkbox = tk.Checkbutton(self.root, text=f"Casilla seleccionable-{opcion}", variable=self.var_reglas[i])
            checkbox.grid(row=i + 1, column=1, sticky="w")

    def procesar(self):
        # Obtener la regla seleccionada
        regla_binaria = "".join(str(var.get()) for var in self.var_reglas)
        regla_decimal = int(regla_binaria, 2)

        # Configurar la regla en el automata
        self.automata.rule = regla_decimal

        # Procesar la generación con la regla seleccionada
        self.automata.procesar_generacion()

        # Actualizar la cuadricula en la interfaz gráfica
        self.actualizar_cuadricula()

    def actualizar_cuadricula(self):
        # Limpiar la cuadricula
        self.canvas.delete("all")

        # Dibujar todas las generaciones en la cuadricula
        for y, generation in enumerate(self.automata.grid):
            for x, cell in enumerate(generation):
                color = "black" if cell == 1 else "white"
                self.canvas.create_rectangle(x * 5, y * 5, (x + 1) * 5, (y + 1) * 5, fill=color)

if __name__ == "__main__":
    # Configuración del automata y la interfaz gráfica
    automata = AutomataCelular(width=110, height=400, rule=150)  # Puedes ajustar el ancho y alto según tus necesidades
    root = tk.Tk()
    interfaz = InterfazGrafica(root, automata)

    # Iniciar la aplicación
    root.mainloop()