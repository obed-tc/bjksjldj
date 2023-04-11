import random

# Lista de posibles mensajes aleatorios
mensajes = ["¡Hola, mundo!", "¡Bienvenidos!", "¡Actualizado automáticamente", "¡Texto aleatorio!"]

# Generar un mensaje aleatorio
mensaje = random.choice(mensajes)

# Abrir y escribir en el archivo README.md
with open("README.md", "w") as f:
    f.write(mensaje)
