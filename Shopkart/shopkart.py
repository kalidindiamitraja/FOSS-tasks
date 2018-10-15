from PIL import Image
import getpass
import random
print("Welcome to the CLI shopkart")
print("Shop By Category")
print("1.Fruits&Vegetables 2.Bakery,Meat&Diary 3.Beverages")
print("4.Snacks            5.Beauty&Hygiene")
kart=[]
quantity=[]
price=[]
a=["Onion","Tomato","Potato","Banana","Apple"]
b=[23,12,33,99,90]
c=["Milk","Bread","Butter","Chicken","Eggs"]
d=[45,30,150,140,50]
e=["Tea","Coffee","Soft Drink","Cold Drink","Water"]
f=[400,610,33,90,20]
g=["Maggi","Pasta","Chips","Chocolate","Ice cream"]
h=[70,80,20,35,200]
i=["Soap","Perfume","Shampoo","Handwash","Powder"]
j=[150,200,150,99,88]
while(True):
	y=input("Enter the category number or enter exit to complete shopping:")
	if(y=="exit"):
		break
	if(int(y)==1):
		print("Fruits&Vegetables")
		print("ITEM NO   ITEM NAME     PRICE")
		print("   1      Onion         Rs 23/kg")
		print("   2      Tomato        Rs 12/kg")
		print("   3      Potato        Rs 33/kg")
		print("   4      Banana        Rs 99/kg")
		print("   5      Apple         Rs 90/set")
		print("For adding into the kart enter in the format itemno space quantity")
		print("Enter exit to exit the category")
		while(True):
			y=input()
			if(y=="exit"):
				break
			else:
				z=list(map(int,y.split()))
				kart.append(a[z[0]-1])
				quantity.append(z[1])
				price.append(z[1]*b[z[0]-1])
	elif(int(y)==2):
		print("Bakery,Meat")
		print("ITEM NO   ITEM NAME     PRICE")
		print("   1      Milk          Rs 45/l")
		print("   2      Bread         Rs 30/pack")
		print("   3      Butter        Rs 150/0.5kg")
		print("   4      Chicken       Rs 140/kg")
		print("   5      Eggs          Rs 50/set")
		print("For adding into the kart enter in the format itemno space quantity")
		print("Enter exit to exit the category")
		while(True):
			y=input()
			if(y=="exit"):
				break
			else:
				z=list(map(int,y.split()))
				kart.append(c[z[0]-1])
				quantity.append(z[1])
				price.append(z[1]*d[z[0]-1])
	elif(int(y)==3):
		print("Beverages")
		print("ITEM NO   ITEM NAME     PRICE")
		print("   1      Tea           Rs 400/kg")
		print("   2      Coffee        Rs 610/0.5kg")
		print("   3      Soft drink    Rs 33/300ml")
		print("   4      Cool drink    Rs 90/2l")
		print("   5      Water         Rs 20/0.5l")
		print("For adding into the kart enter in the format itemno space quantity")
		print("Enter exit to exit the category")
		while(True):
			y=input()
			if(y=="exit"):
				break
			else:
				z=list(map(int,y.split()))
				kart.append(e[z[0]-1])
				quantity.append(z[1])
				price.append(z[1]*f[z[0]-1])
	elif(int(y)==4):
		print("Snacks")
		print("ITEM NO   ITEM NAME     PRICE")
		print("   1      Maggi        Rs 70/pack")
		print("   2      Pasta        Rs 80/pack")
		print("   3      Chips        Rs 20/kg")
		print("   4      Chocolate    Rs 35")
		print("   5      Ice cream    Rs 200/kg")
		print("For adding into the kart enter in the format itemno space quantity")
		print("Enter exit to exit the category")
		while(True):
			y=input()
			if(y=="exit"):
				break
			else:
				z=list(map(int,y.split()))
				kart.append(g[z[0]-1])
				quantity.append(z[1])
				price.append(z[1]*h[z[0]-1])
	elif(int(y)==5):
		print("Beauty&Hygiene")
		print("ITEM NO   ITEM NAME     PRICE")
		print("   1      Soap         Rs 150/pack")
		print("   2      Perfume      Rs 200")
		print("   3      Shampoo      Rs 150")
		print("   4      Handwash     Rs 99")
		print("   5      Powder       Rs 80")
		print("For adding into the kart enter in the format itemno space quantity")
		print("Enter exit to exit the category")
		while(True):
			y=input()
			if(y=="exit"):
				break
			else:
				z=list(map(int,y.split()))
				kart.append(i[z[0]-1])
				quantity.append(z[1])
				price.append(z[1]*j[z[0]-1])	      
for i in range(0,len(kart)):
	print(str(i+1)+" "+kart[i]+" "+str(quantity[i])+" "+str(price[i]))
print(" ")
print("Total   =    "+str(sum(price)))
print("Select payment mode")
print("1.Cash on delivery  2.Credit or Debit Card")
print("* 4% discount on all Credit and Debit cards")
z=int(input())
if(z==1):
	print("Cash on delivery")
else:
	print("Credit or Debit Card")
	x=input("Enter the card number:")
	y=getpass.getpass()
print("Confirm that you are not a robot")
while(True):
	x=random.randint(0,2)
	if(x==0):
		myImage=Image.open('abc1.jpeg')	
	elif(x==1):
		myImage=Image.open('abc2.jpeg')
	else:
		myImage=Image.open('abc3.jpeg')
	width=250
	height=250
	myImage2=myImage.resize((width,height))
	myImage2.show()
	print("Enter the captcha")
	y=input()
	if(x==0):
		if(y=="83tsU"):
			break
		else:
			print("Your entry is wrong")
	elif(x==1):
		if(y=="qGphJD"):
			break
		else:
			print("Your entry is wrong")
	else:
		if(y=="viearer"):
			break
		else:
			print("Your entry is wrong")
if(z==1):
	print("Total Price = "+str(sum(price)))
else:
	print("Total Price = "+str(sum(price)*0.96))
	print("Payment Completed")
print("Thank You")
	
