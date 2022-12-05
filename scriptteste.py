import pytesseract
import cv2

#Lendo a imagem ou grupo de imagens
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
imagem = cv2.imread(r"C:\workspace\pythonworkana\images\exemplo4.jpg")


#Extraindo o texto

texto = pytesseract.image_to_string(imagem)
print(texto)