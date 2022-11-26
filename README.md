# AC:NH auto-painter v1.1
Python script to paint a pattern in AC:NH based on an input image. Made for and tested on Yuzu, using PIL and xdotool.

Right now the bash script this generates is pretty garbage, but it works.

Video example:

[![https://www.youtube.com/watch?v=v6nsk6-SsYM](https://img.youtube.com/vi/v6nsk6-SsYM/0.jpg)](https://www.youtube.com/watch?v=v6nsk6-SsYM)

Input image must be:
* 32x32 pixels
* max 15 colors

Usage:

```bash
# imagemagicks - convert image to 15 colors
convert original.png -colors 15 converted.png

python3 generate.py converted.png
bash output.sh
# right after running the bash script, switch to the window with AC:NH running (cursor must be in top left in the pattern editor) 
```
