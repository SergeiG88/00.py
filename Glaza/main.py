import cv2

# Загрузка классификаторов
face_cascade_path = 'faces.xml'
eye_cascade_path = 'eyes.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Проверка, что классификаторы загрузились правильно
if face_cascade.empty():
    raise IOError(f"Не удалось загрузить классификатор лица из {face_cascade_path}")
if eye_cascade.empty():
    raise IOError(f"Не удалось загрузить классификатор глаз из {eye_cascade_path}")

# Инициализация видеопотока с камеры
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    raise IOError("Не удалось открыть веб-камеру")

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)

while True:
    success, img = webcam.read()

    if not success:
        print("Не удалось получить кадр с веб-камеры")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=6)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (150, 150, 150), thickness=2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=2, minNeighbors=8)

        for (ex, ey, ew, eh) in eyes:
            roi_color2 = roi_color[ey:ey + eh, 0:roi_color.shape[1]]
            roi_color2 = cv2.GaussianBlur(roi_color2, (53, 53), 55)
            roi_color[ey:ey + eh, 0:roi_color.shape[1]] = roi_color2

    img = img[::, ::-1]  # Отражение изображения
    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
