from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def extract_audio_clip(input_video, output_audio, clip_start, clip_end, temp_video='./temp.mp4'):
    ffmpeg_extract_subclip(input_video, clip_start,
                           clip_end, targetname=temp_video)
    ffmpeg_extract_audio(inputfile=temp_video, output=output_audio)


input_video = './nggyu.mp4'
output_audio = './audio.wav'
clip_start = 0
clip_end = 10

extract_audio_clip(input_video, output_audio, clip_start, clip_end)
