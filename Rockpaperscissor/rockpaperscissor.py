from PIL import Image
import random
print("Lets play rock paper scissor")
print("You vs Computer")
a=["rock","paper","scissor"]
x=0
y=0
C=int(input("Max Points:"))
while(True):
	b=input("You:").lower()
	c=random.randint(0,2)
	if(b==a[c]):
		x=x
		y=y
	elif(b=="rock"):
		if(c==1):
			y=y+1
		else:
			x=x+1
	elif(b=="paper"):
		if(c==2):
			y=y+1
		else:
			x=x+1	
	else:
		if(c==0):
			y=y+1
		else:
			x=x+1
	print("Computer:"+a[c])
	print("score="+str(x)+"-"+str(y))
	if(x==C):
		myImage=Image.open('you win.jpeg')
		width=500
		height=500
		myImage2=myImage.resize((width,height))
		myImage2.show()
		break
	elif(y==C):
		myImage=Image.open('youlose2.jpeg')
		width=500
		height=500
		myImage2=myImage.resize((width,height))
		myImage2.show()
		break
