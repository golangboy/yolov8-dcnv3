from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    # load a pretrained model (recommended for training)
    model = YOLO('./ultralytics/cfg/models/v8/yolov8dcn.yaml')
    print(model)
    model.train(data='coco-pose.yaml', epochs=100, imgsz=640)
