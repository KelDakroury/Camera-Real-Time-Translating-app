# Real-Time-Translating-app

The purpose of the project is to facilitate learning new languages through computer-assisted language learning. The idea of the project is to build an app that detects and translates objects in real time. For object detection we use YOLO model trained on the COCO dataset. For the laptop version of the app we use YOLOv5 and for the android version we use YOLOv4 with TFLite because it's computationally less demanding. For trying out the app(s) refer to the next section

## Testing

### Laptop (YOLOv5)

Intall the requirements via `pip3 install -r requirements.txt` and then run `python3 main.py`

### Android app (YOLOv4 with TFLite)

Download and install the apk from [google-drive](https://drive.google.com/file/d/1Gx48kttmMPT5u6n4GA95ywp23GxwEJRt/view?usp=sharing)

### YOLO 9K

We also added an option for detection on image (static not real-time) with Yolo 9k which can detect up to 9000 classes!

In order to build and test the model, you need to run the following commands:
```
> build.sh
> detect.sh image_name.jpg
```

Note that the image has to be inside testing_images directory.

## Demo

<p align="left">
  <img src="https://media1.tenor.com/images/5f00d7d2dafbd476151ade014a8a563f/tenor.gif" width="250"><br/>
</p>
