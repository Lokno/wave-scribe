# Testing script for WaveScribe
# Checks a range of encoding strength variables 
# with conversion to JPEG images of a range of qualities.

from wand.image import Image
from pathlib import Path
import os
import sys

def cmdecho( cmdstr ):
    print(cmdstr)
    os.system( cmdstr )

if len(sys.argv) < 3:
    print ("    usage:  WaveScribeTest.py <test image> <test string> [strength]")
    sys.exit(0)

test_image = Path(sys.argv[1])
test_string = sys.argv[2]

if not test_image.exists():
    print(f"Test image {test_image} not found.")
    sys.exit(0)

if len(sys.argv) > 3 :
    strength = [float(sys.argv[3])]
else:
    strength = [0.15,0.2,0.4,0.6,0.8]

if not os.path.exists("tmp"):
    os.makedirs("tmp")

ws_path = Path("bin/Release/WaveScribe")
if not ws_path.exists():
    print("WaveScribe executable not found. Please compile WaveScribe first.")
    sys.exit(0)

for s in strength:
    img_path = Path(f'tmp/test_{s*10}.png')

    cmdecho(f"{ws_path} {s} {test_image} {img_path} '{test_string}'")
    cmdecho(f"{ws_path} {s} {test_image} {img_path}")

    with Image(filename=img_path) as img:
        with img.convert('jpg') as toJPG:
            print ("converted to jpg")
            with toJPG.convert('png') as backToPNG:
                print ("converted back to png")
                backToPNG.save(filename=img_path)

    cmdecho(f"bin/Release/WaveScribe {s} {img_path}")
    print ("\n")
    
