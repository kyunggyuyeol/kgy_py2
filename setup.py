'''Setup script for object_detection with webrtc'''

from setuptools import find_packages
from setuptools import setup


'''Download the Object Dectection directory'''
import six.moves.urllib as urllib
from zipfile import ZipFile
import os
import re
import shutil



'''Compile Protobufs'''
import subprocess
print("Compiling protobufs")
try:
    subprocess.Popen('protoc object_detection/protos/*.proto --python_out=.', shell=True)

except:
    print("Error compiling Protobufs")
