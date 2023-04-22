import random
import tkinter as tk
from tkinter import ttk

# Creamos las opciones del juego
game_options = ['Piedra', 'Papel', 'Tijeras']


# Comprobamos el ganador
def check_win(choice):
    pc = random.randint(0, 2)
    pc_choice = game_options[pc]
    print("La PC eligió:", pc_choice)

    if choice == 0 and pc == 2:
        final_result = 'Tu ganas!'
        print("Ganaste!")
    elif choice == 1 and pc == 0:
        final_result = 'Tu ganas!'
        print("Ganaste!")
    elif choice == 2 and pc == 1:
        final_result = 'Tu ganas!'
        print("Ganaste!")
    elif choice == pc:
        final_result = 'Empate!'
        print("Empate!")
    else:
        final_result = 'Tu pierdes!'
        print("La PC gana!")
    label_result.config(text=f'Elegiste {game_options[choice]}\nLa PC eligió {pc_choice}, {final_result}')


# Métodos de los eventos
def rock():
    choice = 0
    check_win(choice)


def paper():
    choice = 1
    check_win(choice)


def scissors():
    choice = 2
    check_win(choice)


# Creamos la ventana y le damos caracteristicas
main_window = tk.Tk()
main_window.geometry('600x400')
main_window.title('¡Piedra, Papel o Tijeras!')
main_window.config(background='lightblue')

# Le damos un icono a la ventana
window_icon = tk.PhotoImage(file='icon.png')
main_window.iconphoto(False, window_icon)

# Creamos una etiqueta de bienvenida
label_welcome = ttk.Label(main_window,
                          text="¡Bienvenido a piedra, papel o tijeras!",
                          font=("Helvetica", 12),
                          foreground='black',
                          background='lightblue',
                          wraplength=200,
                          justify='center')
label_welcome.grid(column=1, sticky='NWSE')

# Creamos una etiqueta para el resultado
label_result = ttk.Label(main_window,
                         text="¡Alguien debe ganar!",
                         font="Helvetica",
                         background='lightblue',
                         wraplength=150,
                         justify='center')
label_result.grid(row=3, column=1, columnspan=2, sticky='NSWE', padx=20, pady=20)


# Configurar el grid
main_window.rowconfigure(1, weight=2)
main_window.columnconfigure(0, weight=2)
main_window.columnconfigure(1, weight=2)
main_window.columnconfigure(2, weight=2)

# Le damos estilo a los botones
button_style = ttk.Style()
button_style.theme_use('alt')
button_style.configure('TButton',
                       font=('Helvetica', 12),
                       foreground='blue',
                       background='lightblue',
                       width=20,
                       focuscolor='none')

# Definimos los botones

# Definimos un boton e imagen para piedra
rock_image = tk.PhotoImage(file='rock.png')
rock_image = rock_image.subsample(8, 4)
label_rock = ttk.Label(main_window, image=rock_image)
label_rock.grid(row=1, column=0)
rock_button = ttk.Button(main_window, text='Piedra', command=rock)
rock_button.grid(row=2, column=0, sticky='NSWE', padx=20, pady=50)

# Definimos un boton e imagen para papel
paper_image = tk.PhotoImage(file='paper.png')
paper_image = paper_image.subsample(8, 4)
label_paper = ttk.Label(main_window, image=paper_image)
label_paper.grid(row=1, column=1)
paper_button = ttk.Button(main_window, text='Papel', command=paper)
paper_button.grid(row=2, column=1, sticky='NSWE', padx=20, pady=50)

# Definimos un boton e imagen para las tijeras
scissors_image = tk.PhotoImage(file='scissors.png')
scissors_image = scissors_image.subsample(8, 4)
label_scissors = ttk.Label(main_window, image=scissors_image)
label_scissors.grid(row=1, column=2)
scissors_button = ttk.Button(main_window, text='Tijeras', command=scissors)
scissors_button.grid(row=2, column=2, sticky='NSWE', padx=20, pady=50)

# Iniciamos la ventana hasta que se cierra el programa
main_window.mainloop()
