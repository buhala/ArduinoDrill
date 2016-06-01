from PIL import Image
im = Image.open("image.png") #Can be many different formats.
pix = im.load()
print(im.size)#Get the width and hight of the image for iterating over
#print(pix[x,y]) #Get the RGBA Value of the a pixel of an image
pixels=[]
for i in range(0,20):
	rowPixels=[]
	for m in range(0,20):
		if pix[m,i][0]==0:
			rowPixels.append(1)
			print(1,end="")
		else:
			rowPixels.append(0)
			print(0,end="")
	pixels.append(rowPixels)
	print("")
drillCoords=[0,0] #assuming start at beggining of grid. 
for m in pixels:
	print("moveY(-1)")
	print("moveX(-20)")
	for i in m:
		if i==1:
			asdfasdf=3
			print("moveZ(-1)")
			print("moveZ(1)")