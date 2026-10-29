@echo off
REM Otomatis keluar dari environment lama jika aktif
if defined VIRTUAL_ENV (
    call deactivate
)
REM Aktifkan environment yoloenv310
call "D:\CONVIS PROJEK\yoloenv310\Scripts\activate.bat"
REM Jalankan training YOLOv8
python train_yolo.py
pause
