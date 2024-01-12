import requests
import tkinter as tk
from tkinter import ttk, messagebox

def consultar_pokemon(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verificar si hay errores en la respuesta

        datos_pokemon = respuesta.json()
        return datos_pokemon

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

def limpiar_ceros_izquierda(numero):
    return str(int(numero))  # Convertir a entero y luego a cadena para eliminar ceros a la izquierda

def buscar_pokemon():
    pokemon_id = limpiar_ceros_izquierda(entry_pokemon_id.get())

    if pokemon_id:
        datos_pokemon = consultar_pokemon(pokemon_id)

        if datos_pokemon:
            resultado.config(text=f"Nombre: {datos_pokemon['name']}\nAltura: {datos_pokemon['height']}\nPeso: {datos_pokemon['weight']}")
        else:
            messagebox.showerror("Error", "No se pudieron obtener los datos del Pokémon.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa el ID del Pokémon.")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Consulta de Pokémon")
ventana.configure(bg='#ffffff')  # Fondo blanco

# Elementos de la interfaz con estilos más modernos
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), padding=5, background='#4CAF50', foreground='white')
style.configure('TEntry', font=('Helvetica', 14), padding=5)
style.configure('TLabel', font=('Helvetica', 14), background='#ffffff')

label_instrucciones = ttk.Label(ventana, text="Ingresa el ID del Pokémon:")
entry_pokemon_id = ttk.Entry(ventana)
boton_consultar = ttk.Button(ventana, text="Consultar", command=buscar_pokemon, style='TButton')
resultado = ttk.Label(ventana, text="")

# Posicionamiento de los elementos en la interfaz
label_instrucciones.grid(row=0, column=0, pady=10)
entry_pokemon_id.grid(row=1, column=0, pady=10, ipadx=10, ipady=5)
boton_consultar.grid(row=2, column=0, pady=10, ipadx=10, ipady=5)
resultado.grid(row=3, column=0, pady=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
