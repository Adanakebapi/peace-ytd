from pytube import YouTube
import os, random, sys, subprocess

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ffmpeg = resource_path("ffmpeg.exe")

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

os.system("title PeaceYTD")
os.system("cls")
os.system("color f0")

while True:
    url = input(COLORS["green"]+"Enter the URL: "+COLORS["magenta"])
    try:
        yt = YouTube(url)
    except Exception as e:
        print(COLORS["red"]+"An error has occurred. Please check the URL, if you can't figure out the problem take help from developer. Error Name:",type(e).__name__)
        continue
    itags = []
    for i in yt.streams:
        itags += [str(i.itag)]
    stritags = ""
    for i in yt.streams:
        if i.resolution != None:
            stritags += "["+str(i.itag)+" "+i.mime_type+" "+i.resolution+"], "
        else:
            stritags += "["+str(i.itag)+" "+i.mime_type+"], "
    stritags = stritags[:-2]
    print(COLORS["cyan"]+"Codes:",stritags)
    y = input(COLORS["green"]+"Combine the codes? (Yes/No): "+COLORS["magenta"])
    zz = False
    for i in ["y","yea","ye","yes"]:
        if y.lower() == i.lower():
            zz = True
    if zz:
        while True:
            itag_ = input(COLORS["green"]+"Enter the codes (example: 137,140): "+COLORS["magenta"])
            itag_ = itag_.split(",")
            if (itag_[0] in itags) and (itag_[1] in itags) and (itag_[0] != itag_[1]):
                break
            else:
                print(COLORS["red"]+"An error has occurred. Please retry.")
        for i in yt.streams:
            if str(i.itag) == itag_[0]:
                stream1 = i
            elif str(i.itag) == itag_[1]:
                stream2 = i
        if stream1.mime_type.split("/")[0] == stream2.mime_type.split("/")[0]:
            print(COLORS["red"]+"The selected types are same.")
            continue
        if stream1.mime_type.split("/")[0] == "video":
            video = stream1
            audio = stream2
        else:
            video = stream2
            audio = stream1
        randomf = ""
        for i in range(5):
            randomf += str(random.randint(0,9))
        video_end = video.mime_type.split("/")[1]
        audio_end = audio.mime_type.split("/")[1]
        video.download(filename=f"_video_{randomf}")
        audio.download(filename=f"_audio_{randomf}")
        subprocess.call(['ffmpeg.exe', '-i', f"_audio_{randomf}.{audio_end}", '-i', f"_video_{randomf}.{video_end}", '-c', 'copy', f"CombinedVideo_{randomf}.{video_end}"])
        #ff.output(ff.input(f"_audio_{randomf}.{audio_end}"),ff.input(f"_video_{randomf}.{video_end}"),f"CombinedVideo_{randomf}.{video_end}").run()
        os.remove(f"_audio_{randomf}.{audio_end}")
        os.remove(f"_video_{randomf}.{video_end}")
    else:
        while True:
            itag_ = input(COLORS["green"]+"Enter the Code: "+COLORS["magenta"])
            if itag_ in itags:
                break
            else:
                print(COLORS["red"]+"Can't find the code. Please write a correct code.")
        for i in yt.streams:
            if str(i.itag) == itag_:
                stream_ = i
                break
        randomf = ""
        for i in range(5):
            randomf += str(random.randint(0,9))
        stream_.download(filename=f"_video_{randomf}")
