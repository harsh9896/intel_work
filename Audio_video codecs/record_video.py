import subprocess

# Set up FFmpeg command to capture video from webcam and save to file
input_device = 'video=HP HD Camera'  # change this to your camera device name on Windows
output_file = 'output.mp4' #change it according to codec
video_size = '640x480'
framerate = 30
codec = 'libvpx-vp9' #change it to required codec
bitrate = '2000k'
ffmpeg_command = ['ffmpeg', '-y', '-thread_queue_size', '1024','-f', 'dshow', '-rtbufsize', '1024M', '-video_size', video_size, '-framerate', str(framerate), '-i', input_device, '-t', '3', '-vcodec', codec,  '-preset', 'ultrafast', '-b:v', bitrate, output_file]

# Set up ffplay command to preview the video being captured
ffplay_command = ['ffplay', '-i', output_file]

# Open a subprocess for FFmpeg command to capture video from webcam and save to file
ffmpeg_process = subprocess.run(ffmpeg_command)

# Open another subprocess for ffplay command to preview the video being captured
ffplay_process = subprocess.run(ffplay_command)

# Wait for the FFmpeg process to finish
ffmpeg_process.wait()

# Terminate the ffplay process once the video capture is done
ffplay_process.terminate()