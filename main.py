from ultralytics import YOLO
import cv2

model = YOLO("yolov8s-seg.pt")

results = model.predict(source = "0", show=True)

