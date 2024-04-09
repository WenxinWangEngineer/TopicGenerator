from moviepy.editor import ImageClip, AudioFileClip

# , concatenate_videoclips


def generate_video(image_path, audio_path, duration, filename):
    image_clip = ImageClip(image_path, duration=duration)
    audio_clip = AudioFileClip(audio_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.write_videofile(filename, codec="libx264", fps=24)
