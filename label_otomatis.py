import os

# Path setup
dir_labels = r'd:/CONVIS PROJEK/Potato detection.v11i.yolov8/train/labels'

# Labeling rules
# freshPotato = class 0, rottenPotato = class 1
# Bounding box: seluruh gambar (x_center=0.5, y_center=0.5, width=1.0, height=1.0)
def label_file(fname):
    if fname.lower().startswith('freshpotato'):
        return '0 0.5 0.5 1.0 1.0\n'
    elif fname.lower().startswith('rottenpotato'):
        return '1 0.5 0.5 1.0 1.0\n'
    else:
        return ''  # skip if not match

for fname in os.listdir(dir_labels):
    if fname.lower().endswith('.txt'):
        label = label_file(fname)
        if label:
            with open(os.path.join(dir_labels, fname), 'w') as f:
                f.write(label)

print('Labeling otomatis selesai!')
