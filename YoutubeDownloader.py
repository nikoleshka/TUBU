from pytube import YouTube
from moviepy import AudioFileClip
from tkinter import*

def downloader():
    UserLink = input("Hello, Welcome to My Youtube Downloader \nEnter Your Youtube Link Right Below (-: \n")
    try:
        YT_obj = YouTube(UserLink)
    except Exception as e:
        print("Failed to Connect. Check your network connection. or the availability of your youtube link and run the program again")
        exit()
    UserChoice = input("Great, Now What Format Do you Need? \nEnter 1 for MP4.\nEnter 2 For MP3\n")

    if (UserChoice == "1"):
        while(True):
            user_mp4_quality = input("What Quality do you have in mind?\n Enter 1 for 320p \n Enter 2 for 480p \n Enter 3 for 720p\n")
            if (user_mp4_quality == "1") :
                Quality="320p" 
                break
            elif (user_mp4_quality == '2') :
                Quality ="480p"
                break
            elif (user_mp4_quality == '3'):
                Quality = "720p"
                break
            else: 
                print("Invalid Number! Please Enter a valid one this time (-;\n")
                continue
        
        try:
            Stream = YT_obj.streams.get_by_resolution(Quality)
        except Exception as s:
            exit()
            
        if(Stream):
            Stream.download()
            print("Downloaded Successfully(; \nYou can find the mp4 file in the same folder as this code. Have Fun*")
        else: print("There Was a Problem ):\nCheck if the youtube link is correct and the requested quality is available and Run the program again.\n Goodbye for now.")
    elif(UserChoice == "2"):
        try:
            print("here1")
            mp3 = YT_obj.streams.get_audio_only()
            print("here2")

            audio_file = mp3.download()
            print("here3")
            mp3_filename = audio_file.replace(".mp4", ".mp3")
            audio=AudioFileClip(audio_file).write_audiofile(mp3_filename)
        
            if(audio):
                audio.download()
                print("Downloaded Successfully(; \nYou can find the mp3 file in the same folder as this code. Have Fun*" )
            else: print("There Was a Problem ):\nCheck if the youtube link is correct and the requested quality is available and Run the program again.\n Goodbye for now.")
        except Exception as d:
            print("There Was a Problem ):\nCheck if the youtube link is correct and the requested quality is available and Run the program again.\n Goodbye for now.")

# _____________GUI_____________
root = TK()
window =Label(root, text="youtube downloader")



window.mainloop()





