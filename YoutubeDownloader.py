from pytube import YouTube
UserLink = input("Hello, Welcome to My Youtube Downloader \n Enter Your Youtube Link Right Below (-: \n")
YT_obj = YouTube(UserLink)
UserChoice = input("Great, Now What Format Do you Need? \nEnter 1 for MP4.\n Enter 2 For MP3")
if (UserChoice == 1):
    while(True):
        user_mp4_quality = input("What Quality do you have in mind?\n Enter 1 for 320p \n Enter 2 for 480p \n Enter 3 for 720p")
        if (user_mp4_quality ==1) :
             Quality="320p" 
             break
        elif (user_mp4_quality == 2) :
            Quality ="480p"
            break
        elif (user_mp4_quality ==3):
            Quality = "720p"
            break
        else: 
            print("Invalid Number! Please Enter a valid one this time (-;\n")
            continue
    Stream = YT_obj.streams.get_by_resolution(Quality)
    if(Stream):
        Stream.download()
        print("Downloaded Successfully(; \n You can find the mp4 file in the same folder as this code. Have Fun*")
    else: print("There Was a Problem ):\n Check if the youtube link is correct and the requested quality is available and Run the program again.\n Goodbye for now.")
elif(UserChoice == 2):
    mp3 = YT_obj.streams.get_audio_only()
    if(mp3):
        mp3.download()
        print("Downloaded Successfully(; \n You can find the mp3 file in the same folder as this code. Have Fun*" )
    else: print("There Was a Problem ):\n Check if the youtube link is correct and the requested quality is available and Run the program again.\n Goodbye for now.")





