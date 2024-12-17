import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from ultralytics import YOLO

#Cargar modelo preentrenado de YOLO
model=YOLO('yolo11m-seg.pt')

#Run Inference in the Source
result = model.track(source="/home/santiago/Documentos/Universidad/Practica_Electiva/Rastberry/Imagen1.jpg", show=True, tracker="bytetrack.yaml")