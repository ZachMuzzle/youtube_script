from pytube import YouTube
# from moviepy.editor import VideoFileClip
from tqdm import tqdm
import requests

def download(url, output):
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

url = input("Enter youtube url: ")
output = "/mnt/d/OBS/Videos_from_script"

download(url, output)
