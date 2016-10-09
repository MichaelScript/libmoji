#!/usr/bin/env python
import libmoji
from time import sleep
print("Tesing Loading: ")
sleep(2)
print(libmoji.load_moji(sleep,args=[2],frames=["LOADING.","LOADING..","LOADING..."]))
print("Testing Random Emoji: \n" + libmoji.random())