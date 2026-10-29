from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('Potato detection.v11i.yolov8/yolov8n.pt')
    model.train(
        data='Potato detection.v11i.yolov8/data.yaml',
        epochs=100,
        imgsz=640,
        device=0  # 0 = pakai GPU pertama (RTX 4050)
    )
