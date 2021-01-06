import tkinter as tk
import youtube_dl
import urllib.request
import urllib.parse
import re
import os

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def downloadYouTube(videourl, path):

    ydl_opts = {}
    os.chdir(path)
    global e2
    string1 = e2.get()
    ydl_opts = {
        'format': 'bestaudio/best',              
        'noplaylist' : True,
        'outtmpl': string1,
        'progress_hooks': [my_hook],  
    }
    print(ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videourl])
def dbclick(event):
    item = listbox.get('active')  #get clicked item
    dbclick_cmds[item]()   # run associated command

top = tk.Tk()

top.geometry("800x600")
top.title("Youtube Video Downloader")
def playvideo(video):
    os.system(video)
def printtext():
    global e1
    string = e1.get()
    global e2
    string1 = e2.get()
    query_string = urllib.parse.urlencode({"search_query" : string})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    l = "https://www.youtube.com/watch?v=" + search_results[0]
    downloadYouTube(l, '//home/ayaan/')
    path = '\\home\\ayaan\\'
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.webm' in file:
                files.append(os.path.join(r, file))
            elif '.mp4' in file:
                files.append(os.path.join(r, file))
            elif '.mkv' in file:
                files.append(os.path.join(r, file))
            elif '.avi' in file:
                files.append(os.path.join(r, file))
    for f in files:
        print(f)
        listbox.insert('end',f)
        dbclick_cmds[f] = lambda: playvideo(string1)
l1 = tk.Label(top, text="Enter The Name Or Link Of A Video")
l1.place(x=160, y=250)
l1 = tk.Label(top, text="Enter The File Name")
l1.place(x=240, y=270)
w = tk.Label(top, text="Youtube Video Downloader", font=("Segoe Script", 16))
w.place(x=450, y=0)
e1 = tk.Entry(top)
e1.place(x=350, y=250)

e2 = tk.Entry(top)
e2.place(x=350, y=270)

scrollbar = tk.Scrollbar(top)
scrollbar.pack(side='right', fill='y')

listbox = tk.Listbox(top, yscrollcommand=scrollbar.set)
# dictionary that will contains the function associated to each item
dbclick_cmds = {} 

l1 = tk.Label(top, text="Files Downloaded")

l1.place(x=130, y=0)

listbox.pack(side='left', fill='both')

scrollbar.config(command=listbox.yview)

listbox.bind('<Double-1>', dbclick)


B = tk.Button(top, text ="Download",bg="white",width=15, height=2, command=printtext).place(x=350, y=200)



top.mainloop()
