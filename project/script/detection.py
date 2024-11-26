import cv2
import numpy as np
from datetime import datetime
from .db import *
import time

def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def captura(user_id):
    webcam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("./lib/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("./lib/haarcascade_eye.xml")

    amostra = 0
    numeroAmostras = 5
    largura, altura = 220, 220
    face_confidence_threshold = 5
    eye_confidence_threshold = 5

    print("Capturando as faces. Pressione 'q' para capturar cada foto.")

    connection = get_db_connection()
    cursor = connection.cursor(prepared=True)

    while amostra < numeroAmostras:
        s, video = webcam.read()
        if not s:
            print("Falha ao capturar o frame da webcam")
            break

        video = adjust_gamma(video, gamma=1.5)
        imagemCinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        imagemCinza = cv2.equalizeHist(imagemCinza)

        faces = face_cascade.detectMultiScale(
            imagemCinza,
            scaleFactor=1.1,
            minNeighbors=face_confidence_threshold,
            minSize=(30, 30),
            maxSize=(400, 400)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 2)
            region = imagemCinza[y:y+h, x:x+w]
            
            eyeDetected = eye_cascade.detectMultiScale(
                region,
                scaleFactor=1.1,
                minNeighbors=eye_confidence_threshold,
                minSize=(20, 20)
            )

            if len(eyeDetected) >= 2:
                for (ox, oy, ow, oh) in eyeDetected:
                    cv2.rectangle(video[y:y+h, x:x+w], (ox, oy), (ox + ow, oy + oh), (255, 0, 0), 2)

        cv2.putText(video, f"Amostras: {amostra}/{numeroAmostras}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Detection", video)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            if len(faces) > 0:
                (x, y, w, h) = faces[0]
                imagemFace = cv2.resize(imagemCinza[y:y+h, x:x+w], (largura, altura))
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"face_{amostra+1}_{timestamp}.jpg"
                
                # Convert image to bytes
                _, img_encoded = cv2.imencode('.jpg', imagemFace)
                img_bytes = img_encoded.tobytes()

                # Save to database
                sql = "INSERT INTO fotos (usuario_id, nome_foto, foto, data_captura) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (user_id, filename, img_bytes, datetime.now()))
                connection.commit()

                print(f"Foto {amostra+1} capturada e salva no banco de dados: {filename}")
                amostra += 1
                time.sleep(1)  # Pequena pausa para evitar capturas múltiplas
            else:
                print("Nenhuma face detectada. Tente novamente.")

        if cv2.getWindowProperty("Face Detection", cv2.WND_PROP_VISIBLE) < 1:
            break

    print("Faces capturadas com sucesso")
    cursor.close()
    connection.close()
    webcam.release()
    cv2.destroyAllWindows()
