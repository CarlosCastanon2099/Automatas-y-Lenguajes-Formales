import tkinter as tk

# Lista vacia para guardar las generaciones
generations = []

# THE RULES
rules = {
    '000': 0,
    '001': 1,
    '010': 1,
    '011': 0,
    '100': 1,
    '101': 0,
    '110': 0,
    '111': 1,
}

# Longitud de la generacion
gen_length = 64


# Funcion que crea la ventana y el canvas
def setup():
    global canvas
    root = tk.Tk()
    root.title("Automatas Celulares de Wolfram")
    
    # Se crean las canvas y se les da un tamaño y color
    canvas = tk.Canvas(root, width=800, height=800, bg='black')
    canvas.pack()

    # Se crea la primera generacion 
    generation1 = [1 if i == gen_length // 2 else 0 for i in range(gen_length)]
    generations.append(generation1)

    # Se dibuja la primera generacion y se llama a la funcion next_generation para crear las siguientes
    root.after(250, next_generation)
    root.mainloop()


# Funcion que dibuja las generaciones en el canvas
def draw():
    canvas.delete("all")
    s = 800 / gen_length

    # Se recorre la lista de generaciones y se dibuja cada una de ellas
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


# Se llama a la funcion setup para iniciar el programa (basicamente el main)
if __name__ == "__main__":
    setup()