from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor
import os

def download_video(video_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output file template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio
            'preferredcodec': 'mp3',     # Convert to MP3
            'preferredquality': '320',   # Audio quality
        }],
        'ignoreerrors': True,  # Ignore errors and continue downloading
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_playlist(playlist_url, output_path="downloads", max_workers=4):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Fetch all video URLs in the playlist
    ydl_opts = {
        'extract_flat': True,  # Extract playlist metadata without downloading
        'ignoreerrors': True,  # Ignore errors
    }

    with YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        if not playlist_info:
            print("Failed to fetch playlist information.")
            return

        video_urls = [f"https://www.youtube.com/watch?v={entry['id']}" for entry in playlist_info['entries']]
        print(f"Found {len(video_urls)} videos in the playlist.")

    # Download videos in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_video, url, output_path) for url in video_urls]
        for future in futures:
            future.result()  # Wait for all downloads to complete

    print("Download complete!")

if __name__ == "__main__":
    # Replace with your playlist URL
    playlist_url = "https://music.youtube.com/playlist?list=PLxjOMntBboYpv3jZ0hu3CNdMnHiOW7TSj"
    download_playlist(playlist_url, max_workers=8)  # Adjust max_workers for more parallelism
