from tkinter import *




root1 = Tk()
root1.geometry('1290x500')
root1.title('Capstone Project')
root = Frame(root1)






f1 = Frame(root1)
f1.pack()

f2 = Frame(root1)


f3 = Frame(root1)


f4 = Frame(root1)



f5 = Frame(root1)



f6 = Frame(root1)


f7 = Frame(root1)


f8 = Frame(root1)


f9 = Frame(root1)

one = StringVar()
one.set('Chicken Biryani')

capstone = StringVar()
capstone.set('Chicken Biryani')

secondlast = StringVar()
secondlast.set('Chicken Biryani')

last = StringVar()
last.set('Chicken Biryani')


def page_1():
    label = Label(root, text= 'You will just wait to find out...')
    label.pack()
    btn_sub.configure(state=DISABLED)




    




def next_page():
    f1.pack_forget()
    f2.pack()

def next_page2():
    f2.pack_forget()
    f3.pack()


def next_page3():
    f3.pack_forget()
    f4.pack()


def next_page4():
    f4.pack_forget()
    f5.pack()

def accusations():
    f5.pack_forget()
    f6.pack()


def accusations2():
    f6.pack_forget()
    f7.pack()


def accusations_final():
    f7.pack_forget()
    f8.pack()


def surprise():
    f8.pack_forget()
    f9.pack()


lab_title2 = Label(f1, text= 'Welcome to the Bicycle Mystery Game!\n\n\n Hope you solve the mystery and get ready to use your brain!', font= ('Times New Roman', 16, 'bold'))
lab_title2.pack(pady=50)

lab_btn = Button(f1, text= 'Start your adventure!', font= ('Courier New', 13, 'bold'), command=next_page)
lab_btn.pack(padx=25, pady=20)


lab_title = Label(root, text= 'Behold! The all-new Mystery Game!', font= ('Times New Roman', 16, 'bold'))
lab_title.pack()
lab_intro = Label(root, text= "You walk outside and you find your bike, the new bike you got 30 minutes ago, is missing. You don't know what to do. You've gathered 3 suspects and only one is the true culprit", font= ('Courier New', 11, 'bold'))
lab_intro.pack()


cul1 = Radiobutton(root, text= 'Chicken Biryani', variable = one, value = 'Chicken Biryani')
cul1.pack()
cul2 = Radiobutton(root, text= 'Your annoying, nosy little cousin', variable = one, value = 'Your annoying, nosy little cousin')
cul2.pack()
cul3 = Radiobutton(root, text= 'The landlord of the house', variable = one, value = 'The landlord of the house')
cul3.pack()


btn_sub = Button(root, text= 'Submit your culprit', command=page_1, font= ('Calibri', 14))
btn_sub.pack()






f2_lab = Label(f2, text= 'Chicken Biryani was being eaten at the famous worldwide known resturant.', font= ('Calibri', 14))
f2_lab.pack(pady=10)

f2_lab2 = Label(f2, text= 'The landlord of the house was being sued for millions of dollars.', font= ('Calibri', 14))
f2_lab2.pack(pady=10)

f2_lab3 = Label(f2, text= 'You annoying little cousin is... your daily annoying little cousin.', font= ('Calibri', 14))
f2_lab3.pack(pady=10)



f2_labopt = Radiobutton(f2, variable=capstone, text= 'Your annoying little cousin', value= 'Your annoying little cousin', font= ('Calibri', 14))
f2_labopt.pack()

f2_labopt2 = Radiobutton(f2, variable=capstone, text= 'The landlord of the house', value= 'The landlord of the house', font= ('Calibri', 14))
f2_labopt2.pack()

f2_labopt3 = Radiobutton(f2, variable=capstone, text= 'Chicken Biryani', value= 'Chicken Biryani', font= ('Calibri', 14))
f2_labopt3.pack()


btn_sub2 = Button(f2, text= 'Eliminate a culprit', command=next_page2, font= ('Calibri', 14))
btn_sub2.pack(pady=10)





f3_lab = Label(f3, text= "Chicken Biryani now traveled to the landlord's house, where he sadly got eaten.", font= ('Calibri', 14,))
f3_lab.pack(pady=10)


ques1 = Radiobutton(f3, variable=secondlast, text= 'Your annoying little cousin', value= 'Your annoying little cousin', font= ('Calibri', 14,))
ques1.pack()

ques2 = Radiobutton(f3, variable=secondlast, text= 'The landlord of the house', value= 'The landlord of the house', font= ('Calibri', 14,))
ques2.pack()

ques3 = Radiobutton(f3, variable=secondlast, text= 'Chicken Biryani', value= 'Chicken Biryani', font= ('Calibri', 14))
ques3.pack()


quesans = Button(f3, text= 'Eliminate your culprit', command=next_page3, font= ('Calibri', 14))
quesans.pack(pady=10)


questionforans = Label(f4, text= 'The final text. The final guess. Are you ready to find out who stole your bike?', font= ('Calibri', 14))
questionforans.pack(pady=10)

f4_ans = Button(f4, text= 'Yes! I want to know who stole my bike', command=next_page4, font= ('Calibri', 14))
f4_ans.pack(pady=10)

f4_ans2 = Button(f4, text= 'Welp, there is no going back now so.... why not?', command=next_page4, font= ('Calibri', 14))
f4_ans2.pack(pady=10)


f5_lab = Label(f5, text= 'The landlord is very full after he eats the chicken biryani, so he goes up to your house for a chat with you annoying cousin.', font= ('Calibri', 14))
f5_lab.pack(pady=10)

finalguess1 = Radiobutton(f5, variable=last, text= 'Your annoying little cousin', value= 'Your annoying little cousin', font= ('Calibri', 14))
finalguess1.pack()

finalguess2 = Radiobutton(f5, variable=last, text= 'The landlord of the house', value= 'The landlord of the house', font= ('Calibri', 14))
finalguess2.pack()


finalguess3 = Radiobutton(f5, variable=last, text= 'Chicken Biryani', value= 'Chicken Biryani', font= ('Calibri', 14))
finalguess3.pack()


btn_submit1 = Button(f5, text= 'Eliminate your FINAL culprit', command=accusations, font= ('Calibri', 14))
btn_submit1.pack(pady=10)



accusation1 = Label(f6, text= 'The landlord of the house says that he was eating his food all the time and he was doing exercise. So it could not be me.', font= ('Calibri', 14))
accusation1.pack(pady=10)

accusebtn = Button(f6, text= 'Go on to next subject', command=accusations2, font= ('Calibri', 14))
accusebtn.pack(pady=10)



accusation2 = Label(f7, text= 'Your annoying cousin says he stole a lot of things, but taking your bike would be a whole different level', font= ('Calibri', 14))
accusation2.pack(pady=10)


accusebtn2 = Button(f7, text= 'Final Subject. Click this if you dare.', command=accusations_final, font= ('Calibri', 14))
accusebtn2.pack(pady=10)


accusation3 = Label(f8, text= 'HA HA HA! You never clicked for me. If you did, congratulations! I, the famous Chicken Biryani was the one who stole that petty little bike.\n And guess what bad luck I got. I got eaten by a fat landlord!', font= ('Calibri', 14))
accusation3.pack(pady=10)


accusationbtn = Button(f8, text= 'Click me for instructions to exit!', command=surprise, font= ('Calibri', 14))
accusationbtn.pack(pady=10)


finalgoodbye = Label(f9, text= 'Congratulations! You have found the culprit of the stolen bicycle! Now you are very excited to ride it around the community!\n You go to your house and keep it in a safe place, so that no one will steal it!\n However, you find that it is missing. AGAIN!!! Now it is up to you, in version 2, of the Bicycle Mystery Game!', font= ('Calibri', 14))
finalgoodbye.pack(pady=10)






mainloop()