import sys
import subprocess
from threecolor import app
from flask_frozen import Freezer

freezer = Freezer(app)

#temporary, look into arg parse to do more
if len(sys.argv) > 1 and sys.argv[1] == "build":
    freezer.freeze()
#testing using subprocess to use rync
elif len(sys.argv) > 1 and sys.argv[1] == "rsync":
    print ("calling rsync")
    subprocess.check_call(["rsync", "-avc", "--delete", "gh-pages/", "rsyncoutput/"])
else:
    app.run()
