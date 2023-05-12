import ffmpeg

# input video file
input_file = ffmpeg.input("output.mp3")

# probe the input video file to get codec information
probe = ffmpeg.probe("output.mkv")

# extract video stream information
video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
if len(video_streams) > 0:
    video_stream = video_streams[0]
    video_codec_name = video_stream["codec_name"]
    print("Video codec:", video_codec_name)

# extract audio stream information
audio_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "audio"]
if len(audio_streams) > 0:
    audio_stream = audio_streams[0]
    audio_codec_name = audio_stream["codec_name"]
    print("Audio codec:", audio_codec_name)
