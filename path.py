import os
rootdir = '/root/Downloads/facebook-namanarora921/messages'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))