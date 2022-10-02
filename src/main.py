import cv2
import sys
import pytesseract

#tomado de: https://python.plainenglish.io/text-extraction-in-python-with-neural-networks-2f9ae8512514
if __name__ == "__main__": 
    if len(sys.argv) < 2:
        print("Usage: python ocr_receipt.py receipt.jpg")

    # Leer la ruta de la imagen desde la línea de comandos
    imPath = "src/etiqueta.jpg"

    #Ruta de tesseract
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

    # Parámetros: "-l spa" para utilizar el motor LSTM OCR en español
    config = ("-l spa — oem 1 — psm 3")  

    # Leer la imagen del disco
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)  

    # Ejecutar el OCR de tesseract en la imagen
    texto = pytesseract.image_to_string(im, config=config)  

    # Escribir el texto reconocido en un archivo
    f = open("src/etiqueta_texto.txt", "w")
    f.write(texto)
    f.close()
#tomado de: https://python.plainenglish.io/text-extraction-in-python-with-neural-networks-2f9ae8512514
