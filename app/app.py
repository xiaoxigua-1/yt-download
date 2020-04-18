try:
    import eel
    import pytube
    from pytube import YouTube
    import time
    import os
    import random
except :
    print('你似乎還沒執行過第一次該執行的東西喔')
    input('請關閉程式')
eel.init('app/web')

@eel.expose
def lp(x:str):
    print(x) 
@eel.expose
def ep(x:str,y:str):    
    
    yt = YouTube(x)
    title=str(yt.title)
    eel.pp(f'正在下載{title}的{y}')()
    if y=='mp4':
        
        mp3=str(random.randint(0,1000))
        mp4=str(random.randint(0,1000))
        mp4hd=str(random.randint(0,1000))
        e=os.listdir('app/vo')
        while 1 :
            if mp3+'.mp3' in e or mp4+'.mp4' in e or mp4hd+'.mp4' in e or mp3+'.mp4' in e:
                mp3=str(random.randint(0,1000))+'.mp3'
                mp4=str(random.randint(0,1000))+'.mp4'
                mp4hd=str(random.randint(0,1000))+'.mp4' 
            else :
                break
            
        y=yt.streams.filter(file_extension='mp4',res='1080p')

        if len(y)==0 :
            y=yt.streams.filter(file_extension='mp4',res='720p')
            if len(y)==0:
                y=yt.streams.filter(file_extension='mp4',res='480p')
                if len(y)==0 :
                    y=yt.streams.filter(file_extension='mp4',res='360p')
                    if len(y)==0:
                        y=yt.streams.filter(file_extension='mp4',res='240p')
                        if len(y)==0:
                            y=yt.streams.filter(file_extension='mp4',res='144p')
        eel.pp('下載mp4中')()
        y.first().download(output_path='app/vo',filename=mp4)
        yt.streams.get_highest_resolution().download(output_path='app/vo',filename=mp3)
        eel.pp('下載完成')()
        eel.pp('轉檔中')()
        g2=f'app\\ffmpeg.exe -i app/vo/{mp3}.mp4 -vn -acodec libmp3lame -q:a 0 app/vo/{mp3}.mp3'
        os.system(g2)
        g=f'app\\ffmpeg.exe -i app/vo/{mp3}.mp3 -i app/vo/{mp4}.mp4 -acodec copy -vcodec copy app/vo/{mp4hd}.mp4'
        os.system(g)
        eel.pp('轉檔完成')()
        os.system(f'python app/pp.py app/vo/{mp3}.mp3 app/vo/{mp3}.mp4 app/vo/{mp4}.mp4')
        time.sleep(1)
        os.rename('app/vo/%s.mp4'%mp4hd,'do/%s.mp4'%title)

    elif y=='mp3':
        mp3=str(random.randint(0,1000))
        
        e=os.listdir('app/vo')
        while 1 :
            if mp3+'.mp3' in e or mp3+'.mp4' in e:
                mp3=str(random.randint(0,1000))+'.mp3'

            else :
                break
        eel.pp('下載mp3中')()
        yt.streams.get_highest_resolution().download(output_path='do',filename=mp3)
        eel.pp('下載完成')()
        eel.pp('轉檔中')()
        g2=f'app\\ffmpeg.exe -i do/{mp3}.mp4 -vn -acodec libmp3lame -q:a 0 do/{mp3}.mp3'
        
        
        os.system(g2)
        eel.pp('轉檔完成')()
        os.system(f'python app/pp.py do/{mp3}.mp4')
        time.sleep(1)
        os.rename(f'do/{mp3}.mp3','do/%s.mp3'%title)





eel.start('xiao.html')