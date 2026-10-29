import cv2

def list_available_cameras():
    """
    Mendeteksi semua webcam yang tersedia di sistem
    """
    available_cameras = []
    
    # Coba index 0-10 untuk mencari semua webcam
    for i in range(10):
        try:
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    fps = int(cap.get(cv2.CAP_PROP_FPS))
                    available_cameras.append({
                        'index': i,
                        'resolution': f'{width}x{height}',
                        'fps': fps
                    })
                    print(f"✅ Camera Index {i}: {width}x{height} @ {fps}fps")
                cap.release()
        except Exception as e:
            pass
    
    if not available_cameras:
        print("❌ Tidak ada webcam yang terdeteksi")
        return []
    
    print(f"\n📹 Total {len(available_cameras)} webcam ditemukan")
    return available_cameras

if __name__ == "__main__":
    print("🔍 Scanning available cameras...\n")
    cameras = list_available_cameras()
    
    if cameras:
        print("\n" + "="*50)
        print("Gunakan index berikut di app.py:")
        print("="*50)
        for cam in cameras:
            print(f"Index {cam['index']}: {cam['resolution']} @ {cam['fps']}fps")
