import pytesseract
import cv2

#Lendo a imagem ou grupo de imagens
imagem = cv2.imread("C:\workspace\pythonOCR\images\exemplo2.png")
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"



#Extraindo o texto

texto = pytesseract.image_to_string(imagem)
print(texto)
