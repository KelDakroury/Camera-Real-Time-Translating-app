git submodule uppdate --init --recursive
cd yolo-9000
cat yolo9000-weights/x* > yolo9000-weights/yolo9000.weights
cd darknet 
make
