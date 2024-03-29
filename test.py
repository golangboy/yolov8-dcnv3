from ultralytics import YOLO

if __name__ =='__main__':
    # Load a model
    model = YOLO('./ultralytics/cfg/models/v8/yolov8dcn.yaml')  # load a pretrained model (recommended for training)
    print(model)
    model.train("coco-pose.yaml",epochs=10)
