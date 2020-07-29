from tkinter import *
import random
root = Tk()
root.geometry("400x200")
passtr = StringVar()
passlen = IntVar()
passlen.set(0)
#bahan password+generate
def generate():
	passw = ['a',"b",'c','d','e','f',"g",'h','i','j','k','l','m','n','o',
			'p','q',"r","s","t","u","v","w","x","y","z",'1','2','3','4',
			'5','6','7','8','0','9',"!","#","$",".","@","%","A","B","C","D","E","F","G",
			"H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
			"V","W","X","Y","Z"]
	password = ""
	for x in range(passlen.get()):
		password = password+random.choice(passw)
	passtr.set(password)

Label(root, text="Password Generator by Python 3", font="arial 15 bold").pack()
Label(root, text="Password Length").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text='Generate password now!', command=generate).pack(pady=7)
Entry(root, textvariable=passtr).pack(pady=3)

root.mainloop()