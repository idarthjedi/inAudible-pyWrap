#!/usr/bin/python

import os
import sys


def main():
    """ prompt the user for the directory """

    if len(sys.argv) < 3:
        print("Usage %s [activation bytes] [workingpath]" % sys.argv[0])
        print("For more information see https://github.com/kholia/inAudible")
        exit()

    activationbytes = sys.argv[1]
    workingdirectory = sys.argv[2]
    workingfile = ""
    commandtoexecute = ""
    """ search for all AAX in the directory """

    for file in os.listdir(workingdirectory):
        if file.endswith(".aax"):
            """ split out the names at the first underscore """
            workingfile = file.split("_")[0]
            """ create the output file name """
            commandtoexecute = "ffmpeg -activation_bytes %s -i %s%s -vn -c:a copy %s%s.mp4" % (activationbytes,
                                                                                               workingdirectory,
                                                                                               file,
                                                                                               workingdirectory,
                                                                                               workingfile)
            """ call out to ffmpeg on the command line """
            os.system(commandtoexecute)


main()
