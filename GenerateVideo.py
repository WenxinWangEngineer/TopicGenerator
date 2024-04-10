from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def generate_video(image_paths, audio_paths, duration, filename):
    image_clips = []
    for image_path in image_paths:
        image_clip = ImageClip(image_path, duration)
        image_clips.append(image_clip)

    video_clip = concatenate_videoclips(image_clips)

    audio_clips = []
    for audio_path in audio_paths:
        audio_clip = AudioFileClip(audio_path, duration)
        audio_clips.append(audio_clip)

    video_clip = video_clip.set_audio(audio_clips)

    video_clip.write_videofile(filename, codec="libx264", fps=24)
