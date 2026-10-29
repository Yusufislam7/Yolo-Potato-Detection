import os
import shutil

# Path setup
dir_fresh = r'd:/CONVIS PROJEK/Fresh'
dir_rotten = r'd:/CONVIS PROJEK/Rotten'
dir_images = r'd:/CONVIS PROJEK/Potato detection.v11i.yolov8/train/images'
dir_labels = r'd:/CONVIS PROJEK/Potato detection.v11i.yolov8/train/labels'

# Make sure label folder exists
os.makedirs(dir_labels, exist_ok=True)

def move_and_create_labels(src_dir):
    for fname in os.listdir(src_dir):
        if fname.lower().endswith('.jpg'):
            src_path = os.path.join(src_dir, fname)
            dst_path = os.path.join(dir_images, fname)
            # Move image
            shutil.move(src_path, dst_path)
            # Create empty label file
            label_name = os.path.splitext(fname)[0] + '.txt'
            label_path = os.path.join(dir_labels, label_name)
            if not os.path.exists(label_path):
                with open(label_path, 'w') as f:
                    pass  # Empty label file

move_and_create_labels(dir_fresh)
move_and_create_labels(dir_rotten)

print('Selesai! Semua gambar dipindahkan dan file label kosong dibuat.')
