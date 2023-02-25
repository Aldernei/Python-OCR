import pytesseract
import cv2

# Lendo a imagem
imagem = cv2.imread("images/exemplo2.png")

# Verificando se a imagem foi lida corretamente
if imagem is None:
    print("Erro ao ler a imagem")
else:
    # Configurando o caminho do executável do Tesseract
    caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = caminho_tesseract

    # Extraindo o texto da imagem
    try:
        texto = pytesseract.image_to_string(imagem)
        print(texto)
    except Exception as e:
        print("Erro ao extrair texto da imagem:", e)
