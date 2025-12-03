import yt_dlp
import sys

def download_videos(url):

    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_captions_only(url,index='',lang='en'):
    ydl_opts = {
        'skip_download': True,         
        'writesubtitles': True,        
        'writeautomaticsub': True,      
        'subtitleslangs': [lang],       
        'subtitleformat': 'srt',        
        'outtmpl': f'{index}_'+'%(title)s.%(ext)s' 
        
    }

def main_menu():
    
    while True:
        print("\n========= YouTube Video Downloader CLI =========")
        print("1. Download single video (best quality)")
        print("2. Download captions only")
        print("0. Exit")
        choice = input("Choose an option (0-2): ").strip()

        if choice == "1":
            url = input("Enter video URL: ")
            download_videos(url)

        elif choice == "2":
            url = input("Enter video URL: ")
            index = input("Optional - Enter file prefix: ").strip()
            lang = input("Subtitle language (default = 'en'): ").strip() or 'en'
            download_captions_only(url, index, lang)
        
        elif choice == "0":
            print("Exiting... Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter a number from 0 to 2.")

if __name__ == "__main__":
    main_menu()