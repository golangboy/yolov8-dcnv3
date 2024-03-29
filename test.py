from ultralytics import YOLO

if __name__ =='__main__':
    # Load a model
    model = YOLO('ultralytics/ultralytics/cfg/models/v8/yolov8dcn.yaml')  # load a pretrained model (recommended for training)
