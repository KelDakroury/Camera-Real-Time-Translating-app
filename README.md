# Real-Time-Translating-app

The purpose of the project is to facilitate learning new languages through computer-assisted language learning. The idea of the project is to build an app that detects and translates objects in real time. For object detection we use YOLO model trained on the COCO dataset. For the laptop version of the app we use YOLOv5 and for the android version we use YOLOv4 with TFLite because it's computationally less demanding. For trying out the app(s) refer to the next section

## Testing

**Laptop (YOLOv5)**

Intall the requirements via `pip3 install -r requirements.txt` and then run `python3 main.py`

**Android app (YOLOv4 with TFLite)**

Download and install the apk `real-time translator.apk` from the root directory into your android phone

In order to build and test the model, you have to run the following commands:
```
> build.sh
> detect.sh image_name.jpg
```

Note that the image has to be inside testing_images directory.
