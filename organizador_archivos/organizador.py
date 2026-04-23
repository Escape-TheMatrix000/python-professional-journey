import os
import shutil

ruta = "C:/Users/isaac/Downloads"

tipos = {
    "imagenes": [".jpg", ".png", ".jpeg"],
    "documentos": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".mkv"]
}

for archivo in os.listdir(ruta):
    nombre, extension = os.path.splitext(archivo)

    for carpeta, extensiones in tipos.items():
        if extension.lower() in extensiones:
            carpeta_destino = os.path.join(ruta,carpeta)
        
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            shutil.move(
                os.path.join(ruta,archivo),
                os.path.join(carpeta_destino,archivo)
            )
    nombre_base, extension = os.path.splitext(archivo)
    contador = 1

    ruta_destino = os.path.join(carpeta_destino, archivo)

    while os.path.exists(ruta_destino):
        nuevo_nombre = f"{nombre_base}_{contador}{extension}"
        ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
        contador += 1
        
        shutil.move(
            os.path.join(ruta, archivo),
            ruta_destino
        )
