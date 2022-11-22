import time
import cv2
import yolov5
from googletrans import Translator


def get_yolov5_model(size='n'):
    model_name = f'yolov5{size}.pt'
    model = yolov5.load(model_name)
    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = True  # NMS multiple labels per box
    model.max_det = 5  # maximum number of detections per image
    model._get_name
    return model


def yolov5_process(model, frame):
    results = model(frame)
    new_frame = results.render()[0]
    return new_frame

def translate_model_classes(model, target_lang='ru'):
    translator = Translator()
    for i in range(len(model.names)):
        translated_name = translator.translate(model.names[i], src='en', dest=target_lang).text
        model.names[i] = f'{model.names[i]} ({translated_name})'

if __name__ == '__main__':
    # load pretrained model
    model = get_yolov5_model(size='n')
    translate_model_classes(model)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Can't open source")
        exit()

    w, h = (1280, 720)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # writer = cv2.VideoWriter('output.mp4', fourcc, 30, (w, h))

    # Read until video is completed
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        old_time = time.time()
        frame = yolov5_process(model, frame)
        print(type(frame))
        new_time = time.time()

        cv2.imshow('Frame', frame)

        # writer.write(frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    # writer.release()