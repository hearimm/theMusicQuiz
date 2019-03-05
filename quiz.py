import mp3play
import os
import random
import time

BASE_DIR = os.path.abspath(".\\resources") + "\\"
l = [f for f in os.listdir(BASE_DIR) if f.endswith(".mp3")]

answer = random.randint(0, len(l)-1)
clip = mp3play.load(BASE_DIR+l[answer])
req = -1
while(req != answer):
    sec = int(input("몇 초를 열까요?: "))
    clip.play(sec * 1000, (sec+1)*1000)

    for item in l:
        print(str(l.index(item)) + " : " + item)
    time.sleep(1)
    clip.stop()
    req = int(input("정답은?!:"))
    if req == answer:
        print("정답: " + l[answer])
        break
    print("땡!")
