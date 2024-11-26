from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import cv2
import csv
from datetime import datetime
from db import *


camera = cv2.VideoCapture(0)
detectorFace = cv2.CascadeClassifier("./lib/haarcascade_frontalface_default.xml")
detectorEye = cv2.CascadeClassifier("./lib/haarcascade_eye.xml")  # Add eye detector
#reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("./lib/classificadorLBPH.yml")

largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
id_t = ''

nome_arquivo = 'ponto.csv'
hora = datetime.now()

connection = get_db_connection()
cursor = connection.cursor(dictionary=True)

def gerar_arquivo(resultado):
    with open(nome_arquivo, "a+", newline="") as csvfile:
        dados = csv.writer(csvfile)
        tempo = (resultado, hora, '\n')
        dados.writerow(tempo)

def get_user_name(user_id):
    try:
        cursor.execute("SELECT nome FROM usuario WHERE cod = %s", (int(user_id),))
        result = cursor.fetchone()
        return result['nome'] if result else "Usuário não encontrado"
    except mysql.connector.Error as err:
        print(f"Erro de banco de dados: {err}")
        return "Erro no banco de dados"

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, minNeighbors=20, minSize=(30, 30), maxSize=(400, 400))
    
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 255), 2)
        
        # DETECTA OS OLHOS NO ROSTO
        roi_gray = imagemCinza[y:y+a, x:x+l]
        roi_color = imagem[y:y+a, x:x+l]
        eyes = detectorEye.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # RECONHECE OS OLHOS
        if len(eyes) >= 2:
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            
            imagemFace = cv2.resize(roi_gray, (largura, altura))
            id, confianca = reconhecedor.predict(imagemFace)
            id_t = id

            cursor.execute("SELECT nome FROM usuario WHERE cod = %s", (int(id),))
            resultado = cursor.fetchall() 

            nome = get_user_name(id)
            if not resultado:
                cv2.putText(imagem, "Nenhum user encontrado", (x, y + (a + 30)), font, 2, (0, 0, 255))
            else:
                cv2.putText(imagem, nome, (x, y + (a + 30)), font, 1, (0, 255, 0), 2)

            
            if confianca < 100:  # Ajuste este valor conforme necessário
                cv2.putText(imagem, nome, (x, y + (a + 30)), font, 1, (0, 255, 0), 2)
            else:
                cv2.putText(imagem, "Baixa confianca", (x, y + (a + 30)), font, 1, (0, 0, 255), 2)

        else:
            cv2.putText(imagem, "Olhos nao detectados", (x, y + (a + 30)), font, 2, (255, 0, 0))

    cv2.imshow("Face", imagem)

    if cv2.waitKey(1) == ord('q'):
        gerar_arquivo(nome)
        break

    if cv2.getWindowProperty("Face", cv2.WND_PROP_VISIBLE) < 1:
        break

camera.release()
cv2.destroyAllWindows()