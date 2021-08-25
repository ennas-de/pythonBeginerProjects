from tkinter import *
# import pytube


root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Youtube Downloader")

Label(root, text = "Youtube Video Downloader", font = 'ail 20 bold').pack()

#enter link
link = StringVar()

Label(root, text = "Paste your download link here:", font = 'arial 15 bold').place(x= 100, y = 60)

link_entry = Entry(root, width = 50, textvariable = link).place(x = 32, y = 90)

# function to download video

def Download():
    d_url = YouTube(str(link.get()))
    video = d_url.streams.first()
    video.download()

    label(root, text = "DOWNLOADED", font = 'arial 15').place(x = 180, y = 210)

Button(root, text = 'Download', font = 'arial 15', bg = 'blue', padx = 2, command = Download).place(x = 190, y = 150)

root.mainloop()
