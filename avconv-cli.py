#!/usr/bin/env python3

import glob
import subprocess
import os


song_list = glob.glob('*.mp3')

os.mkdir('converted')

for i in song_list:
    subprocess.call(['avconv', '-i', i, '-b', '96k', 'converted/' + i[:-3] + 'm4a'])

