import cv2

for i in range(5):
    cap = cv2.VideoCapture(i, cv2.CAP_MSMF)
    if cap.isOpened():
        print(f"✅ Webcam ditemukan di index {i}")
        cap.release()
