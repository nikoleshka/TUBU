from pytube import YouTube
from moviepy import AudioFileClip
import tkinter as tk
from tkinter import messagebox, filedialog

def downloader(UserLink, UserChoice, user_mp4_quality):
    try:
        YT_obj = YouTube(UserLink)
    except Exception:
        messagebox.showerror("Error", "Failed to connect. Check your network or the YouTube link.")
        return

    if UserChoice == "1":
        Quality = {"1": "320p", "2": "480p", "3": "720p"}.get(user_mp4_quality, None)
        if not Quality:
            messagebox.showerror("Error", "Invalid quality selected.")
            return
        stream = YT_obj.streams.get_by_resolution(Quality)
        if stream:
            stream.download()
            messagebox.showinfo("Success", "MP4 downloaded successfully.")
        else:
            messagebox.showerror("Error", "Stream not found for selected quality.")
    elif UserChoice == "2":
        try:
            mp3 = YT_obj.streams.get_audio_only()
            audio_file = mp3.download()
            mp3_filename = audio_file.replace(".mp4", ".mp3").replace(".webm", ".mp3")
            AudioFileClip(audio_file).write_audiofile(mp3_filename)
            messagebox.showinfo("Success", "MP3 downloaded successfully.")
        except Exception:
            messagebox.showerror("Error", "Audio download/conversion failed.")


def start_download():
    link = enterlink.get()
    format_choice = format_var.get()
    quality_choice = quality_var.get()
    
    step3.pack_forget()
    downloader(link, format_choice, quality_choice)


def go_to_step2():
    step1.pack_forget()
    step2.pack()


def handle_format_choice():
    format_choice = format_var.get()
    step2.pack_forget()
    if format_choice == "1":
        step3.pack()
    else:
        downloader(enterlink.get(), "2", None)  # No quality for MP3


# GUI Setup _____________________________
root = tk.Tk()
root.title("TUBU")
root.configure(background="red")
root.geometry("500x300")
root.minsize(200, 200)
root.maxsize(500, 500)

# Shared Control Variables
format_var = tk.StringVar()
quality_var = tk.StringVar()

# Step 1
step1 = tk.Frame(root)
tk.Label(step1, text="Welcome to TUBU", font=("Helvetica", 12),fg="white",activebackground="red", activeforeground="red").pack(pady=20)
tk.Label(step1, text="Enter your YouTube link:", font=("Arial", 12),fg="white",activebackground="red", activeforeground="red").pack(pady=20)

enterlink = tk.Entry(step1, width=50)
enterlink.pack()
tk.Button(step1, text="Next", command=go_to_step2).pack(pady=20)

# Step 2
step2 = tk.Frame(root)
tk.Label(step2, text="Select format:", font=("Arial", 12),fg="red",bg="white").pack(pady=20)
tk.Radiobutton(step2, text="MP4", variable=format_var, value="1").pack(anchor="w")
tk.Radiobutton(step2, text="MP3", variable=format_var, value="2").pack(anchor="w")
tk.Button(step2, text="Next", command=handle_format_choice).pack(pady=10)

# Step 3 (Quality selection)
step3 = tk.Frame(root)
tk.Label(step3, text="Select video quality:", font=("Arial", 12),fg="red",bg="white").pack(pady=20)
tk.Radiobutton(step3, text="320p", variable=quality_var, value="1").pack(anchor="w")
tk.Radiobutton(step3, text="480p", variable=quality_var, value="2").pack(anchor="w")
tk.Radiobutton(step3, text="720p", variable=quality_var, value="3").pack(anchor="w")
tk.Button(step3, text="Download", command=start_download).pack(pady=10)

# Start with step 1
step1.pack()

root.mainloop()
