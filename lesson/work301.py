import os
for files in os.listdir():
    print("%s 【%dBytes】" % (files, os.path.getsize(files)))
