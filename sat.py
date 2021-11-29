import os
os.system ("tmate -S /tmp/tmate.sock new-session -d")
os.system ("tmate -S /tmp/tmate.sock wait tmate-ready")
os.system ("tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'")

 



