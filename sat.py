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
 

 


cmdline ('tmate -S /tmp/tmate.sock new-session -d && tmate -S /tmp/tmate.sock wait tmate-ready && tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'')
