cd yolo-9000/darknet

./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000-weights/yolo9000.weights ../../testing_images/$1

xdg-open predictions.jpg