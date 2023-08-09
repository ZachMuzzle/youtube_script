from pytube import YouTube
# from moviepy.editor import VideoFileClip
from tqdm import tqdm
import requests
import subprocess
def download_video(url, output):
    try:
        youtube = YouTube(url)

        video_stream = youtube.streams.get_highest_resolution()

        video_title = youtube.title
        file_size = video_stream.filesize
        output = output + f"/{str(video_title)}.mp4"
        # print(output)
        response = requests.get(video_stream.url, stream=True)

        #progress bar
        progress_bar = tqdm(total=file_size, unit='bytes', unit_scale=True, desc=f"Downloading {video_title}")

         # Download the video in chunks and update the progress bar
        with open(output, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))

        progress_bar.close()
        # video_stream.download(output_path=output,filename_prefix="video", on_progress_callback=lambda chunk, file_handle, bytes_remaining: progress_bar.update(file_size - bytes_remaining))

        print("Download has been completed!")

        print("Conversion complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def audio_download(url, output):
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Get the highest quality audio stream
        audio_stream = youtube.streams.filter(only_audio=True).first()

        # Download the audio
        audio_stream.download(output_path=output)

        # Rename the downloaded audio file with an MP3 extension
        audio_file = audio_stream.default_filename
        mp3_file = audio_file[:-4] + ".mp3"
        new_file_path = f"{output}/{mp3_file}"
        current_file_path = f"{output}/{audio_file}"
        import os
        os.rename(current_file_path, new_file_path)

        subprocess.call(['ffmpeg', '-i', new_file_path, f'{output}/{mp3_file}'])

        print("Extraction complete!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

decision = input("Enter in Video or Audio: ")
if(decision == 'Video' or decision == 'video' or decision == 'v' or decision == 'V'):
    url = input("Enter youtube url: ")
    output = "/mnt/g/Editing/OBS/Videos_from_script"
    download_video(url, output)
elif(decision == 'Audio' or decision == 'audio' or decision == 'a' or decision == 'A'):
    url = input("Enter youtube url: ")
    output = "/mnt/g/Editing/OBS/Videos_from_script/Audio"
    audio_download(url, output)
