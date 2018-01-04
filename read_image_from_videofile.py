#install sudo apt-get install ffmpeg module

import subprocess

img_output_path='/give path to save frame/'
subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:05.000', '-vframes', '1', img_output_path])
