# An OEIS wallpaper generator
```
$ python oeiswall.py -h

usage: oeiswall.py [-h] [--bgcolor [BGCOLOR]] [--size [SIZE [SIZE ...]]]
                   [--font [FONT]] [--numSize [NUMSIZE]] [--txtSize [TXTSIZE]]
                   [--namSize [NAMSIZE]] [--numColor [NUMCOLOR]]
                   [--txtColor [TXTCOLOR]] [--namColor [NAMCOLOR]] [--n [N]]
                   [--out [OUT]]

Create a wallpaper using OEIS

optional arguments:
  -h, --help            show this help message and exit
  --bgcolor [BGCOLOR]   bgcolor
  --size [SIZE [SIZE ...]]
                        size
  --font [FONT]         font
  --numSize [NUMSIZE]   font size of numbers
  --txtSize [TXTSIZE]   font size of text
  --namSize [NAMSIZE]   font color of name
  --numColor [NUMCOLOR]
                        font color of numbers
  --txtColor [TXTCOLOR]
                        font size of text
  --namColor [NAMCOLOR]
                        font size of name
  --n [N]               OEIS index
  --out [OUT]           name of output file
```
## Example
```
$ python oeiswall.py
```
will produce some white on black wallpaper from some random OEIS sequence from A000001 to A000100.

```
$ python oeiswall.py --n 27 --namColor #63b8ff 
```
produces <https://imgur.com/Z183Pau>
