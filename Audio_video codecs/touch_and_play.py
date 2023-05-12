import cv2
import subprocess as sp
import numpy as np

# Set up FFmpeg command for capturing video from the webcam
input_device = 'video=USB Camera'
output_file = 'output.mp4'
video_size = '640x480'
framerate = 30
codec = 'libx264'
bitrate = '2000k'

ffmpeg_cmd = [
    'ffmpeg',
    '-y',  # overwrite output file if it already exists
    '-f', 'dshow',  # force DirectShow input
    '-i', input_device,  # input device (webcam)
    '-t', '5',
    '-s', video_size,  # video size
    '-r', str(framerate),  # framerate
    '-vcodec', codec,  # video codec
    '-b:v', bitrate,  # video bitrate
    output_file  # output file
]

# Open the FFmpeg subprocess
proc = sp.Popen(ffmpeg_cmd, stdin=sp.PIPE, stderr=sp.PIPE)

# Set up OpenCV window to display video from webcam
cv2.namedWindow('Webcam Capture', cv2.WINDOW_NORMAL)

# Capture and display video from webcam until 'q' key is pressed
while True:
    # Read frame from the video stream
    # print("Harsh")
    ret, frame = cv2.VideoCapture(0).read()

    # Display the frame in the OpenCV window
    cv2.imshow('Webcam Capture', frame)

    # Check if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close OpenCV window and FFmpeg subprocess
cv2.destroyAllWindows()
proc.stdin.write('q'.encode())
proc.stdin.flush()
proc.wait()
