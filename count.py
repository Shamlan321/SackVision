import argparse
import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import *  # Assuming tracker.py defines the Tracker class
from datetime import datetime
import os

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Count sacks in a video file or webcam stream.')
    parser.add_argument('-f', '--filename', type=str, help='Input video file name')
    parser.add_argument('-d', '--device_id', type=int, help='Device ID of the webcam (e.g., 0 for integrated webcam)')
    args = parser.parse_args()

    # If neither filename nor device_id is provided, prompt the user for input
    if args.filename is None and args.device_id is None:
        args.filename = input("Enter the filename (or press Enter to use webcam): ")

    # Initialize video capture based on provided argument
    start_time = datetime.now()  # Record the start time
    timestamp_str = start_time.strftime("%d/%m/%Y %H:%M:%S")
    datetime_str = start_time.strftime("%d_%m_%Y_%H_%M_%S")
    output_filename = f"{datetime_str}_processed.mp4"

    # Ensure the 'processed' directory exists
    if not os.path.exists("processed"):
        os.makedirs("processed")
    output_filepath = os.path.join("processed", output_filename)

    try:
        if args.filename:
            cap = cv2.VideoCapture(args.filename)  # Use the filename provided as argument
            y = 475  # Adjust this value for file input
        elif args.device_id is not None:
            cap = cv2.VideoCapture(args.device_id)  # Use the device ID provided as argument
            y = 350  # Adjust this value for webcam input
        else:
            # Prompt user for device ID if webcam option is selected
            device_id = input("Enter the device ID of the webcam (e.g., 0 for integrated webcam): ")
            cap = cv2.VideoCapture(int(device_id))
            y = 350  # Adjust this value for webcam input
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return
    except ValueError:
        print("Invalid device ID. Please provide a valid integer device ID.")
        return

    # Check if the video capture object is successfully initialized
    if not cap.isOpened():
        print("Error: Unable to open video source.")
        return

    # Get frame rate of input video
    fps = cap.get(cv2.CAP_PROP_FPS) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30

    # Define the codec and create VideoWriter object
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_filepath, fourcc, fps, (frame_width, frame_height))

    model = YOLO('yolov8_custom.pt')

    class_list = ['sack-d3vD']
    tracker = Tracker()
    count = 0

    down = {}
    counter_down = set()
    previous_count = 0  # To track changes in counter

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        count += 1

        results = model.predict(frame)

        a = results[0].boxes.data
        a = a.detach().cpu().numpy()
        px = pd.DataFrame(a).astype("float")

        list = []

        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]
            if 'sack-d3vD' in c:
                list.append([x1, y1, x2, y2])

        bbox_id = tracker.update(list)

        offset = 7

        for bbox in bbox_id:
            x3, y3, x4, y4, id = bbox
            cx = int(x3 + x4) // 2
            cy = int(y3 + y4) // 2

            if y < (cy + offset) and y > (cy - offset):
                down[id] = cy
                if id in down:
                    cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                    cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)
                    cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
                    counter_down.add(id)

        text_color = (255, 255, 255)
        red_color = (0, 0, 255)
        green_color = (0, 255, 0)

        cv2.line(frame, (10, y), (1004, y), red_color, 3)  # Adjust y-coordinate based on input source

        downwards = len(counter_down)
        cv2.putText(frame, 'Sacks Counted: ' + str(downwards), (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, red_color, 2, cv2.LINE_AA)

        # Write the frame to the output video
        out.write(frame)

        # Display the frame
        cv2.imshow("frames", frame)

        # Break the loop when 'Esc' is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Write the final counter value to the log file
    with open('count.log', 'a') as file:
        log_entry = f"{timestamp_str},{downwards}\n"
        file.write(log_entry)

    # Release video capture and writer objects
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
