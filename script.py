import yt_dlp
import shutil
""" Main downloader used now. Uses YT_DLP """
def download_video2(url):
    """ 
    Method for downloading youtube videos using yt_dl

    Parameters
    ----------
    url: pass in a Youtube url
     """
    ydl = yt_dlp.YoutubeDL()
    try:
        options = {
            'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
            'outtmpl': '/mnt/g/Editing/OBS/Videos_from_script/%(title)s.%(ext)s',
        }
        with ydl:
            result = ydl.extract_info(url,download=True, extra_info=options)
        print("Download was completed!")
        #Transfer file to another location
        video_title = result.get('title', 'video')
        videoId = result['id']
        file_extension = result.get('ext', 'mkv')
        file_name = f"{video_title} [{videoId}].{file_extension}"
        # TODO: Look into reading title and seeing if word in title matches a folder 
        print(file_name)
        # Setup env for these paths
        source_path = f"/home/zachmuzzle/youtube_script/{file_name}"
        dest_path = f"/mnt/g/Editing/OBS/Videos_from_script/"
        shutil.move(source_path, dest_path)
        print("Move was completed!")
    except Exception as e:
        print(f"{(e)}")

def audio_download_dlp(link): 
    """ 
    Method for downloading audio from Youtube videos using yt_dl

    Parameters
    ----------
    url: pass in a Youtube url 
     """
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as video:
        info_dict = video.extract_info(link, download = True)
        video_title = info_dict['title']
        print(video_title)
        video.download(link)    
        print("Successfully Downloaded - see local folder on Google Colab")

if __name__ == "__main__":
    decision = input("Enter in Video or Audio: ")
    if(decision == 'Video' or decision == 'video' or decision == 'v' or decision == 'V'):
        url = input("Enter youtube url: ")
        output = "/mnt/g/Editing/OBS/Videos_from_script"
        audioOutput = "/mnt/g/Editing/OBS/Videos_from_script/Audio"
        download_video2(url)
    elif(decision == 'Audio' or decision == 'audio' or decision == 'a' or decision == 'A'):
        url = input("Enter youtube url: ")
        output = "/mnt/g/Editing/OBS/Videos_from_script/Audio"
        audio_download_dlp(url)
