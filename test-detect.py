import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', device='cpu')  # or yolov5n - yolov5x6, custom

#if torch.cuda.is_available():
#  device = 'cuda'
#else:
#  device = 'cpu'
#model.to(device)

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
