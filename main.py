import os
import re
from pytube import Playlist
from moviepy.editor import VideoFileClip


def download_playlist_videos(playlist_link, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    playlist = Playlist(playlist_link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    try:
        playlist.download(download_dir, max_downloads=5000)  # Download up to 50 videos simultaneously
    except Exception as e:
        print(f"Error while downloading: {e}")


def extract_audio_from_videos(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    videos = os.listdir(input_directory)
    for video_file in videos:
        video_path = os.path.join(input_directory, video_file)
        output_file_name = os.path.splitext(video_file)[0] + ".mp3"
        output_path = os.path.join(output_directory, output_file_name)

        try:
            video = VideoFileClip(video_path)
            video.audio.write_audiofile(output_path)
            video.close()
        except Exception as e:
            print(f"Error while extracting audio: {e}")


if __name__ == "__main__":
    playlist_link = ''
    download_dir = 'D:\Video'
    audio_output_dir = 'D:\Video\songs'

    download_playlist_videos(playlist_link, download_dir)
    extract_audio_from_videos(download_dir, audio_output_dir)
