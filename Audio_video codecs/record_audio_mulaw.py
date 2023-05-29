import subprocess

# Set up FFmpeg command to capture audio from microphone and save to file
input_device = 'audio=Microphone Array (Intel® Smart Sound Technology (Intel® SST))'  # change this to your audio device name on Windows
output_file = 'output.mkv' #change it according to codec
codec = 'pcm_mulaw' #change it to required codec
bitrate = '16k'
sample_rate='8k'
ffmpeg_command = ['ffmpeg', '-y', '-f', 'dshow', '-i', input_device, '-t', '10', '-acodec', codec, '-b:a', bitrate,  output_file]

# Set up ffplay command to preview the audio being captured
ffplay_command = ['ffplay', '-i', output_file]

# Open a subprocess for FFmpeg command to capture audio from microphone and save to file
ffmpeg_process = subprocess.run(ffmpeg_command)

# Open another subprocess for ffplay command to preview the audio being captured
ffplay_process = subprocess.run(ffplay_command)

# Wait for the FFmpeg process to finish
ffmpeg_process.wait()

# Terminate the ffplay process once the audio capture is done
ffplay_process.terminate()
# 
