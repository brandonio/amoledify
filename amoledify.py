from PIL import Image

def amoledify(pic, bg=(0, 0, 0), fg=None):
	img = Image.open(pic)
	pixels = list(img.getdata())

	i = 56
	new = []
	for p in pixels:
		if p[0] <= i:
			new.append(bg)
		elif fg:
			new.append(fg)
		else:
			new.append(p)

	img.putdata(new)
	del pixels, new
	return img