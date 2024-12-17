from ultralytics import YOLO
import cv2
import numpy as np

Pixel_to_cm = 25                       #xx pixels are 1cm (assumption, needs to be calibrated in real time) 
Pixel_to_square_cm = 25*25

# Load a pretrained segmentation model
model = YOLO('yolo11n-seg.pt')

# Run inference on an image
img = cv2.imread("/home/santiago/Documentos/Universidad/Practica_Electiva/Rastberry/Imagen5.png")
H, W, _ = img.shape
results = model(img, show=True, save=True)


for result in results:
    for j, mask in enumerate(result.masks.data):
        mask = mask.numpy() 
        mask_output = mask *255

        mask = cv2.resize(mask, (W, H))

        area = np.sum(mask)
        print(f"Object {j} area (in pixels): {area}")
        
        total_area_cm = round(area / Pixel_to_square_cm, 0)
        print(f"Object area (in cm2): {total_area_cm}")
        
        cv2.imwrite('./output .png', mask_output)