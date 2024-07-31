# About
SackVsion is a computer vision project that uses YOLOv8 for detection and ByteTrack for tracking to count sacks in real-time. It offers real-time counting of sacks, it can also work on pre-recorded video. After processing the video is output video is also saved in the `processed` folder. You can also train your own YOLO model to count custom objects according to your needs.
# Demo
   ![Alt Text](https://github.com/Shamlan321/SackVision/blob/main/Demo1.gif)
# Usage
1. To use this project, execute the following commands one-by-one:
   ```
   git clone https://github.com/Shamlan321/SackVision/

   cd SackVision

   pip install -r requirements.txt

   python3 count.py
   ```
 
2. If everything is installed, the script will start.
![Alt Text](https://github.com/Shamlan321/SackVision/blob/main/SS.png)

3. Now, there are two options, you can either drop a pre-recorded video in the terminal or you can enter the camera device id for real-time processing. Like most of the time `0` is the     id of internal webcam and if you have an external camera attached, it would be something like `1` or `2`. 
4. :warning: Based on your camera resolution you may need to adjust the counting line to your needs. 
5. After processing a `log.txt` will be saved which contains the total number of detections on a certain date and time. The output video will also be saved in the `processed` directory.

# Features
1. Trained on 500+ images dataset. [Roboflow Dataset](https://universe.roboflow.com/huui/engro-sack/dataset/1)
2. Works both on CPU and GPU (should have CUDA support and drivers).
3. Automatically creates `log.txt` which keeps track of total detections on specific time.
4. Creates an output video for post-analysis.
5. Can be used for Custom Object Counting (Read Below).

# Custom Training:
If you want to count objects other than sacks, you can train your own YOLOv8 model for that and use it with this project. Follow the steps below:

1. Follow this detailed guide for custom training. [Roboflow Guide](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset)   [Video Guide](https://www.youtube.com/watch?v=wuZtUMEiKWY&t=547s)
2. Rename the custom downloaded model to `yolov8_custom.pt` and move it into the `SackVision` directory.
3. Edit the `count.py` file and change line 66, `class_list = ['sack-d3vD']` to your object class name, e.g for dog it will be `class_list = ['dog']`.
4. Save and run the script.
