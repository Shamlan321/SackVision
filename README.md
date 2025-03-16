![Alt Text](https://wheat-rail-813665.hostingersite.com/SACK.png)



# SackVision: Precise Object Counting, Real-Time Insights. 📦🔍

**Taglines:**

* "Transforming visual data into actionable counts."
* "Real-time object counting made simple and accurate."
* "From sacks to anything: Customize your counting needs."

SackVision is a cutting-edge computer vision project designed to provide accurate, real-time object counting. By combining the power of YOLOv8 for object detection and ByteTrack for robust object tracking, SackVision offers a versatile solution for various counting applications. Whether you need to count sacks in a warehouse, monitor traffic flow, or track any other type of object, SackVision delivers reliable results.

## Demo
![Cool Animation](Demo1.gif)


## Why SackVision?

In today's data-driven world, precise object counting is crucial for optimizing operations, improving efficiency, and gaining valuable insights. SackVision streamlines this process, automating the counting task and eliminating the need for manual, error-prone methods. This project is not limited to counting sacks; its adaptability allows you to train custom models for any object, making it a powerful tool for a wide range of industries.

## Key Features: Unveiling the Power

* **Real-Time Object Detection and Tracking:**
    * Leverages YOLOv8, a state-of-the-art object detection model, for accurate and fast detection.
    * Employs ByteTrack for robust object tracking, ensuring consistent counts even in challenging environments with occlusions or fast-moving objects.
* **Versatile Video Processing:**
    * Processes live video streams from webcams or IP cameras, providing real-time counting.
    * Supports pre-recorded video files, allowing you to analyze existing footage.
* **Customizable Object Counting:**
    * Empowers users to train their own YOLOv8 models for counting any custom object.
    * Provides a simple workflow for integrating custom models into the project.
* **Comprehensive Logging and Reporting:**
    * Automatically generates a `log.txt` file that records the total count of detections along with the date and time, enabling detailed analysis.
    * Creates output video files with the bounding boxes and tracked objects for post analysis.
* **Hardware Agnostic:**
    * Optimized for both CPU and GPU, ensuring flexibility for different hardware configurations.
    * GPU acceleration (CUDA required) provides significant performance improvements for real-time processing.
* **Pre-Trained Model Included:**
    * Comes with a pre-trained YOLOv8 model for sack counting, trained on a dataset of 500+ images from [Roboflow Dataset](https://universe.roboflow.com/huui/engro-sack/dataset/1), allowing you to get started quickly.
* **Adjustable Counting Lines:**
    * Allows the user to modify the counting line within the code, to adjust for different camera angles and resolution.

## Getting Started: A Step-by-Step Guide

### Prerequisites

* Python 3.x (recommended 3.8 or higher)
* Git
* (Optional) CUDA enabled GPU with drivers installed.

### Installation

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/Shamlan321/SackVision/](https://github.com/Shamlan321/SackVision/)
    cd SackVision
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Script:**

    ```bash
    python3 count.py
    ```

### Usage Instructions

1.  **Input Selection:**
    * The script will prompt you to enter a video file path or a camera device ID.
    * For camera input, enter the device ID (e.g., `0` for the default webcam).
    * For video input, drag and drop the video file into the terminal.
2.  **Counting Line Adjustment:**
    * Open the `count.py` file and locate the line where the counting line coordinates are defined.
    * Adjust the coordinates based on your camera view and desired counting area.
3.  **Output and Logging:**
    * The processed video with detected and tracked objects will be saved in the `processed` directory.
    * A `log.txt` file containing the total count and timestamp will be created in the project directory.

## Custom Training: Tailoring SackVision to Your Needs

1.  **Dataset Preparation:**
    * Gather a dataset of images or videos of the objects you want to count.
    * Annotate the objects in your dataset using tools like Roboflow or LabelImg.
2.  **YOLOv8 Training:**
    * Follow a comprehensive guide on training YOLOv8 on a custom dataset, such as the [Roboflow Guide](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset) or a relevant [Video Guide](https://www.youtube.com/watch?v=wuZtUMEiKWY&t=547s).
3.  **Model Integration:**
    * Rename your trained YOLOv8 model to `yolov8_custom.pt`.
    * Replace the existing `yolov8_custom.pt` file in the SackVision directory with your trained model.
4.  **Class List Modification:**
    * Open the `count.py` file and modify the `class_list` variable (line 66) to match the class names of your custom objects.
5.  **Run the Script:**
    * Execute `python3 count.py` to start counting your custom objects.

## Contributing

We welcome contributions from the community! Feel free to submit pull requests, report bugs, or suggest new features.

## License

This project is licensed under the MIT License.
