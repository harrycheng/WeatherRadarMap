import time 
import datetime
import os.path
import imageio

from urllib.request import urlretrieve      

def urllib_download(src, des):      
    print(src + " to " +des)
    try:
        urlretrieve(src, des)   
    except:
        print('error ' + src + " to " + des)

def generatorMinutePic():    
    now = datetime.datetime.now()        
    minute = now.minute - now.minute % 6
    now = now.replace(minute=minute)
    
    baseTime = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, 0)    
    deltaMinute = datetime.timedelta(days=0, hours=0, minutes=6, weeks=0, seconds=0,milliseconds=0, microseconds=0)
    preTime = now - deltaMinute
    while(preTime > baseTime):
        minuteName = preTime.strftime('%Y%m%d%H%M00000.PNG')
        picPath = './img/' +  minuteName
        
        if not os.path.isfile(picPath) :
            urllib_download(generatorBaseSrc() + minuteName, picPath)

        #time.sleep(1)
        preTime = preTime - deltaMinute        
        
        

def generatorBaseSrc():
    #http://image.nmc.cn/product/2018/05/17/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_AZ9010_L88_PI_20180517063000000.PNG
    now = datetime.datetime.now()    

    url = 'http://image.nmc.cn/product/'
    dateStr = now.strftime('%Y/%m/%d/')
    bjLocation = "RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_AZ9010_L88_PI_"    
    srcPath = '%s%s%s' % (url, dateStr, bjLocation)
    return srcPath

def generatorGif():
    images = []
    workDir = os.getcwd()
    filenames = sorted( fn for fn in os.listdir('./img') if fn.endswith('.PNG') )        
    for filename in filenames:        
        filePath = '%s/img/%s' % (workDir, filename)
        images.append(imageio.imread(filePath))
    imageio.mimsave(datetime.datetime.now().strftime('%Y%m%d') + 'weather.gif', images, duration=0.5, loop=1)  # duration 每帧间隔时间，loop 循环次数
    print('完成……')

#generatorMinutePic()
generatorGif()

