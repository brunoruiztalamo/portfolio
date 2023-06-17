from PIL import Image, ImageEnhance
import os

def main():
    filename = r'ruta/a/imagen.png'
    image = Image.open(filename)

    # Aplicar mejoras a la imagen
    enhancer = ImageEnhance.Sharpness(image)
    resultado1 = enhancer.enhance(1.0)

    enhancer = ImageEnhance.Color(resultado1)
    resultado2 = enhancer.enhance(1.0)

    enhancer = ImageEnhance.Contrast(resultado2)
    resultado3 = enhancer.enhance(1.0)

    enhancer = ImageEnhance.Brightness(resultado3)
    resultado4 = enhancer.enhance(1.0)
    
       # Obtener el nombre del archivo y la extensión para proximamente sobreescribir
    nombre_archivo, extension = os.path.splitext(filename)

    # Generar el nuevo nombre con el sufijo
    nuevo_nombre = f"{nombre_archivo}_01{extension}" 
    # Se puede cambiar "01" por el sufijo deseado

    # Obtener la ruta completa del archivo modificado
    ruta_modificada = os.path.join(r'ingrese la imagen', nuevo_nombre)
    print("Ruta completa del archivo modificado:", ruta_modificada)
    
    # Guardar la imagen modificada en la ubicación especificada
    try:
        resultado4_rgb = resultado4.convert("RGB")
        resultado4_rgb.save(ruta_modificada, format='JPEG')
        print("Imagen guardada exitosamente.")
    except Exception as e:
        print("Error al guardar la imagen:", e)

if __name__ == "__main__":
    main()



