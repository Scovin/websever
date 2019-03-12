import sys
import subprocess
import re

def GetImage(path):
    Name = ['unknown']
    cmd1 = 'source /Users/liyicong/DL/bin/activate'
    cmd2 = 'cd /Users/liyicong/darknet'
    cmd3 = './darknet detect cfg/yolov3.cfg yolov3.weights '+path
    p = subprocess.Popen(cmd1+'&&'+cmd2+"&&"+cmd3, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        Str = line.decode("utf-8")
        if Str.find('%')  == -1:
            pass
        else:
            regex = re.sub(r'\d|:|%|\s','', Str)
            Name.append(regex)
    return Name

