#!/usr/bin/python3

import os


buff = " Lorem ipsum dolor\n sit amet consectetur \n adipisicing elit "
with open("txt", mode='w', encoding="utf-8") as FILE:
    FILE.write(buff)
print(f"file node before first open {FILE.mode}")
with open("txt", encoding="utf-8") as FILE:
    print(FILE.read())
# os.rename("txt", "TEXT")
# os.remove("TEXT")
os.mkdir("TSTDIR")
os.chdir("TSTDIR")
print("Cur Dir", os.getcwd())
os.chdir("..")
print("Cur Dir", os.getcwd())
os.removedirs("TSTDIR")
