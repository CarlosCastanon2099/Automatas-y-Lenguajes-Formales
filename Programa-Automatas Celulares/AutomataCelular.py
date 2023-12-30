import tkinter as tk

# Lista vacia para guardar las generaciones
generations = []

# Diccionario para almacenar las reglas
rules = {
    '111': 0,
    '110': 0,
    '101': 0,
    '100': 0,
    '011': 0,
    '010': 0,
    '001': 0,
    '000': 0,
}

# Longitud de la generacion
gen_length = 64

# Funcion que crea la ventana y el canvas
def setup():
    global canvas
    root = tk.Tk()
    root.title("Automatas Celulares de Wolfram")

    # Diccionario para almacenar los botones de reglas
    rule_buttons = {}

    # Funcion para cambiar el estado de la regla
    def toggle_rule(rule):
        rules[rule] = 1 - rules[rule]
        update_rule_buttons()

    # Funcion para generar una nueva configuracion
    def generate():
        global generations
        generations = []
        generation1 = [1 if i == gen_length // 2 else 0 for i in range(gen_length)]
        generations.append(generation1)
        update_rule_buttons()
        draw()

    # Funcion que dibuja las generaciones en el canvas
    def draw():
        canvas.delete("all")
        s = 800 / gen_length

        for j, gen in enumerate(generations):
            for i, cell in enumerate(gen):
                if cell == 1:
                    canvas.create_rectangle(i * s, j * s, (i + 1) * s, (j + 1) * s, fill='white')

    # Funcion que crea las siguientes generaciones y las guarda en la lista de generaciones 
    def next_generation():
        last_gen = generations[-1]
        next_gen = []

        for i in range(len(last_gen)):
            rule = ''.join(str(last_gen[j]) if 0 <= j < len(last_gen) else '0' for j in range(i - 1, i + 2))
            next_gen.append(rules[rule])

        generations.append(next_gen)

        if len(generations) > 32:
            generations.pop(0)

        draw()
        canvas.after(250, next_generation)

    # Funcion para actualizar el estado de los botones de reglas en la interfaz
    def update_rule_buttons():
        for rule, button in rule_buttons.items():
            button.config(text=f"casilla seleccionable-{rule} ({rules[rule]})", relief=tk.SUNKEN if rules[rule] else tk.RAISED)

    # Se crean las canvas y se les da un tamaño y color
    canvas = tk.Canvas(root, width=800, height=800, bg='black')
    canvas.pack()

    # Se crean los botones de reglas
    for rule in rules:
        rule_buttons[rule] = tk.Button(root, text=f"casilla seleccionable-{rule} ({rules[rule]})", command=lambda r=rule: toggle_rule(r))
        rule_buttons[rule].pack(side=tk.LEFT)

    # Se crea el boton para generar una nueva configuracion
    generate_button = tk.Button(root, text="Generar", command=generate)
    generate_button.pack(side=tk.LEFT)

    # Se llama a la funcion generate para iniciar el programa
    generate()

    # Se llama a la funcion next_generation para iniciar la generacion automática
    root.after(250, next_generation)
    root.mainloop()

# Se llama a la funcion setup para iniciar el programa (basicamente el main)
if __name__ == "__main__":
    setup()