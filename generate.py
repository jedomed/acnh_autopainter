from PIL import Image
import sys

im = Image.open(sys.argv[1])
im = im.convert('HSV')
pix = im.load()

x_axis = im.size[0]
y_axis = im.size[1]

final_script = "sleep 1; "
time = "0.03"
time_key = "0.02"

reverse = False
palette = []
palette_pos = 0;

def pressKey(key, time_key_fce = time_key):
	global final_script
	final_script += "sleep " + time + ";xdotool keydown " + key + ";sleep " + time_key_fce + ";xdotool keyup " + key + ";"

def sleep(time_fce):
	global final_script
	final_script += "sleep " + time_fce + ";"

for y in range(0, y_axis):
	for x in range(0, x_axis):
		color = pix[x,y]
		if color not in palette:
			if (len(palette) > 15):
				break
			palette.append(color)
			# print(color)
		if (len(palette) > 15):
			break

# print(len(palette))

pressKey("v")
pressKey("w")
pressKey("d")
pressKey("c")	

for color in palette:
	hue = round(color[0]/255*30)
	saturation = round(color[1]/255*15)
	value = round(color[2]/255*15)
	
	sleep(time)
	pressKey("a");pressKey("a");pressKey("a");pressKey("a");
	sleep(time); pressKey("a", "2.1")
	
	for i in range(0, hue):
		pressKey("d")
	
	pressKey("s")
	pressKey("a"); sleep(time);	pressKey("a", "1.8")
	for i in range(0, saturation):
		pressKey("d")
	
	pressKey("s")
	pressKey("a"); sleep(time);	pressKey("a", "1.8")
	for i in range(0, value):
		pressKey("d")
	
	pressKey("e")
	pressKey("w")
	pressKey("w")

pressKey("c")
pressKey("x")
sleep("0.7")
pressKey("x")

for color in palette:
	pressKey("q")
	
sleep(time)
pressKey("q")

for y in range(0, y_axis):
	if (reverse):
		key = "a"
	else:
		key = "d"
		
	for x in range(0, x_axis):
		x_temp = x;
		if (reverse):
			x_temp = x_axis-x-1
				
		# print("y: " + str(y) + "; x: " + str(x_temp))
		
		atLeastOne = False
		for index, color in enumerate(palette):
			if (pix[x_temp,y] == color):
				atLeastOne = True
				if (palette_pos < index):
					for i in range(0, index-palette_pos):
						pressKey("e")
				elif (palette_pos > index):
					for i in range(0, abs(index-palette_pos)):
						pressKey("q")
				palette_pos = index
		atLeastOne = False
			
		if (pix[x_temp,y] != (255, 255, 255, 255)):
			final_script += "xdotool keydown c; sleep " + time_key + "; xdotool keyup c; "
		
		if (x != (x_axis-1)):
			pressKey(key)
		final_script += "sleep " + time + "; "
		
	pressKey("s")
	reverse = not reverse

print(final_script, file=open('output.sh', 'w'))
