# Introduction
This is a python script used to loop through all aax files in a given directory and 
complete the backup/conversion process to mp4 using the inAudible framework.

This has only been tested in Windows 10, Python 3.6 and ffmpeg-20180127-a026a3e-win64-static

# Anti-Piracy Notice
Please only use this script for gaining access to content you are licensed to use for archiving/conversion/convenience. 
DeDRMed content should not be uploaded to open servers, torrents, or other methods of mass distribution. 
No help will be given to people doing such things. Authors, retailers, and publishers all need to make a living, 
so that they can continue to produce content for us to enjoy. 

Don’t be a parasite.

This blurb is borrowed from the https://apprenticealf.wordpress.com/ page.

## Step 1
Follow the steps outlined at https://github.com/kholia/inAudible to setup your environment

## Step 2
Use the Audible Manager to download your files into a local directory 
(you do not need to authenticate them if you have completed step 1)

## Step 3
Run the program using the following syntax

python convert.py [activation bytes] [directory with aax files]

### Results
This code will remove all the extraneous names at the end of the file, and create an MP4 (chapter preserving) 
file with the same name as the original file (minus all the extra names)
