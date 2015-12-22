from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from random import randint
import requests
import argparse

# argparse
parser = argparse.ArgumentParser(description='Create a wallpaper using OEIS')
parser.add_argument('--bgcolor', nargs='?', type=str, default='#2b2b2b',
                    help='bgcolor')
parser.add_argument('--size', nargs='*', type=int, default=[1920, 1080],
                    help='size')
parser.add_argument('--font', nargs='?', type=str, default="DejaVuSansMono.ttf",
                    help='font')
parser.add_argument('--numSize', nargs='?', type=int, default=50,
                    help='font size of numbers')
parser.add_argument('--txtSize', nargs='?', type=int, default=30,
                    help='font size of text')
parser.add_argument('--namSize', nargs='?', type=int, default=60,
                    help='font color of name')
parser.add_argument('--numColor', nargs='?', type=str, default="white",
                    help='font color of numbers')
parser.add_argument('--txtColor', nargs='?', type=str, default="white",
                    help='font size of text')
parser.add_argument('--namColor', nargs='?', type=str, default="white",
                    help='font size of name')
parser.add_argument('--n', nargs='?', type=int, default=-1,
                    help='OEIS index')
parser.add_argument('--out', nargs='?', type=str, default="",
                    help='name of output file')
args = parser.parse_args()

img = Image.new("RGB", args.size, args.bgcolor)
numFont = ImageFont.truetype(args.font, args.numSize)
txtFont = ImageFont.truetype(args.font, args.txtSize)
namFont = ImageFont.truetype(args.font, args.namSize)
draw = ImageDraw.Draw(img)

if args.n < 0:
    n = randint(1, 100)
else:
    n = args.n

name = 'A' + str(n).zfill(6)
url = "https://oeis.org/" + name

# scraper
r = requests.get(url)
html = r.text.split('\n')
sequence = next(x for x in html if "<tt>" in x).replace(
    ' ', '')[4:-5].split(',')
infoIndex = html.index(next(x for x in html if "<td valign=top align=left>" in
                            x)) + 1
info = html[infoIndex].strip(' ')
wrapped = wrap(info, width=30)
info = "\n".join(wrapped)

# drawer
draw.text((.1 * args.size[0], .2 * args.size[1]), name, font=namFont,
          fill=args.namColor)
draw.text((.1 * args.size[0], .3 * args.size[1]), info, font=txtFont,
          fill=args.txtColor)
for i in range(len(sequence)):
    draw.text((0.7 * args.size[0], (0.08 * i + 0.07) * args.size[1]),
              str(sequence[i]),
              font=numFont,
              fill=args.numColor)

if args.out == "":
    img.save(name + ".jpg", 'JPEG')
else:
    img.save(args.out, 'JPEG')
