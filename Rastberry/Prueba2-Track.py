from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO('yolo11n-seg.pt')

# Specify the source image
source = '/home/santiago/Documentos/Universidad/Practica_Electiva/Rastberry/Imagen2.jpg'
# source = 0

# Make predictions
# results = model.predict(source, save=True, imgsz=320, conf=0.5)
results = model.predict(source, show=True, tracker="bytetrack.yaml", save=True, imgsz=320, conf=0.5)

# Extract bounding box dimensions
boxes = results[0].boxes.xywh.cpu()
for box in boxes:
    x, y, w, h = box
    print("Width of Box: {}, Height of Box: {}".format(w, h))

# Sacar la mascara con result.mask, luego contar sus pixeles 1 para asi sacar la medida