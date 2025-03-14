import random
import string
import secrets
import tkinter as tk
from tkinter import messagebox

def generar_contrasena(longitud=6):
    """Genera una contraseña segura con longitud mínima de 6 caracteres."""
    if longitud < 6:
        longitud = 6
    
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    contraseña = [
        secrets.choice(letras_minusculas),
        secrets.choice(letras_mayusculas),
        secrets.choice(digitos),
        secrets.choice(caracteres_especiales)
    ]
    
    todos_caracteres = letras_minusculas + letras_mayusculas + digitos + caracteres_especiales
    
    while len(contraseña) < longitud:
        contraseña.append(secrets.choice(todos_caracteres))
    
    secrets.SystemRandom().shuffle(contraseña)
    return ''.join(contraseña)

def verificar_fortaleza(contraseña):
    """Verifica si la contraseña cumple con requisitos mínimos."""
    tiene_minuscula = any(c.islower() for c in contraseña)
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_digito = any(c.isdigit() for c in contraseña)
    tiene_especial = any(c in string.punctuation for c in contraseña)
    longitud_suficiente = len(contraseña) >= 6
    return all([tiene_minuscula, tiene_mayuscula, tiene_digito, tiene_especial, longitud_suficiente])

def generar_y_mostrar():
    """Función para generar y mostrar la contraseña en la interfaz."""
    try:
        longitud = int(entry_longitud.get())
        nueva_contraseña = generar_contrasena(longitud)
        es_segura = verificar_fortaleza(nueva_contraseña)
        label_resultado.config(text=f"Contraseña: {nueva_contraseña}\n¿Es segura? {es_segura}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x200")

# Etiqueta y entrada para la longitud
label_longitud = tk.Label(ventana, text="Longitud deseada (mínimo 6):")
label_longitud.pack(pady=10)

entry_longitud = tk.Entry(ventana)
entry_longitud.insert(0, "6")  # Valor por defecto cambiado a 6
entry_longitud.pack()

# Botón para generar contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_y_mostrar)
boton_generar.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", wraplength=350)
label_resultado.pack(pady=10)

# Iniciar la interfaz
ventana.mainloop()
