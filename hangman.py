import sys



def os():
    import os
    name=os.name
    if name.lower().startswith("nt"):
        return 0
    if name.lower().startswith("linux"):
        return 1
    if name.lower().startswith("os"):
        return -1
    return name


def get_python_version():
    import sys
    version=int(sys.version.split(".")[0])
    if version is 2:
        return True
    else:
        return False

def get_command_to_type(package):
    python_version=None
    if os() is 0:
        if get_python_version():
            python_version="python"
        else:
            python_version="py"
    else:
        if get_python_version():
            python_version="python"
        else:
            python_version="python3"
    return "{} -m pip install {}".format(python_version,package)

try:
    from tkinter import *
except:
    print("Please type the following command: \n\t{}".format(get_command_to_type("tkinter")))
    exit(1)

try:
    import sentry_sdk
except:
    print("Please type the following command: \n\t{}".format(get_command_to_type("sentry-sdk")))


'''
Checking if a letter is in the word
'''
def is_letter_in_word(letter,word):
    response=False
    for i,c,status in word:
        if c==letter:
            word[i]=new_tuplet=(i,c,True)
            response=True
    return response

'''
returning the word as a list of tuples containing the position the character and wether the character should be visible or not
'''
def get_word_as_string(word):
    letters=[]
    for i,c in enumerate(word):
        if c==" ":
            tupple=(i,c,True)
        else:
            tupple=(i,c,False)
        letters.append(tupple)
    return letters

'''
Checking if all the letters are visible. If they are, then the game is over
'''
def game_is_over(word):
    result=True
    for i,c,status in word:
        result=result and status
    return result


'''
returning the word in a printable form, All the letters that are not found are printed using the _ character
'''
def get_word(word):
    response=""
    for i,c,status in word:
        if status:
            response=response+c
            if c==" ":
                response=response+"  "
        else:
            response=response+"_ "
    return response.strip()


'''
Creating a gui using tkinter to get the desirable word
'''
def gui_for_word_input():
    window=Tk()
    window.bind('<Return>', lambda e: window.destroy())

    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    lbl=Label(window, text="Word to be found:", fg='red', font=("Helvetica", 11))
    lbl.place(x=20, y=50)

    content_word = StringVar()
    word_entry=Entry(window, text="", bd=5,show="*",textvariable=content_word)
    word_entry.place(x=150, y=50)
    word_entry.focus_set()

    submit=Button(window, text="Submit Word",command=window.destroy, fg='blue')
    submit.place(x=80, y=100)
    
    window.title('Enter Word')
    window.geometry("300x200+{}+{}".format(windowWidth//2,windowHeight//2))
    window.mainloop()
    return str(content_word.get())



'''
function to check if the character entered by the user is in word and applying the desirable changes.
'''
def check_entry(window,string_entered,lost_letters,word_label,lost_letters_label_text,word):

    if len(lost_letters)>7:
        print(len(lost_letters))
        window.destroy()
        lost_gui()
        return None

    char=string_entered.get()
    is_or_not=is_letter_in_word(char,word)
    if not is_or_not:
        lost_letters.append(char)
        lost=" ".join(lost_letters).strip().replace(" ",", ")
        lost_letters_label_text.set("{}={}".format(lost_letters_label_text.get().split("=")[0],lost))
    else:
        word_string=get_word(word)
        word_label.set("{}={}".format(word_label.get().split("=")[0],word_string))
        if game_is_over(word):
            window.destroy()
            cheers_gui()
    string_entered.set("")

'''
A gui created to congratulate the user
'''
def cheers_gui():
    window=Tk()
    window.bind('<Return>', lambda e: window.destroy())
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    lbl=Label(window, text="Congratulations!!! You won!!!", fg='red', font=("Helvetica", 11))
    lbl.place(x=20, y=50)

    window.focus_force()
    window.title('Congratulations!!')
    window.geometry("300x200+{}+{}".format(windowWidth//2,windowHeight//2))
    window.mainloop()

'''
A gui created for when the user loses
'''
def lost_gui():
    window=Tk()
    window.bind('<Return>', lambda e: window.destroy())
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    lbl=Label(window, text="Sorry!!! You lost!!!\nBetter Luck Next Time", fg='red', font=("Helvetica", 11))
    lbl.place(x=20, y=50)

    window.focus_force()
    window.title('Game Is Over!!')
    window.geometry("300x200+{}+{}".format(windowWidth//2,windowHeight//2))
    window.mainloop()

'''
The main gui of the app that enables the user to interact
'''
def general_gui(word,lost_letters):
    lost=" ".join(lost_letters).strip().replace(" ",", ")
    window=Tk()
    #window.bind('<Return>', lambda e: window.destroy())

    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()

    word_label_test=StringVar()
    lbl=Label(window,textvariable=word_label_test, fg='red', font=("Helvetica", 11))
    word_label_test.set("Word = {}".format(get_word(word)))
    lbl.place(x=20, y=50)

    
    lbl=Label(window, text="Character:", fg='red', font=("Helvetica", 11))
    lbl.place(x=20, y=90)

    content_word = StringVar()
    word_entry=Entry(window, text="", bd=5,textvariable=content_word)
    word_entry.place(x=150, y=90)
    word_entry.focus_set()

    lost_letters_text=StringVar()
    lost_letters_label=Label(window, textvariable=lost_letters_text, fg='red', font=("Helvetica", 11))
    lost_letters_text.set("Letters That Do Not Exist = {}".format(lost))
    lost_letters_label.place(x=20, y=180)

    word_entry.bind("<KeyRelease>",lambda e: check_entry(window,content_word,lost_letters,word_label_test,lost_letters_text,word))

    exit=Button(window, text="Exit",command=window.destroy, fg='blue')
    exit.place(x=80, y=125)

    window.title('Enter Word')
    window.geometry("300x200+{}+{}".format(windowWidth//2,windowHeight//2))
    window.focus_force()
    window.mainloop()


sentry_sdk.init("https://9560b462153a44cd89e9e79c6725b2e6@sentry.io/1536897")
word=get_word_as_string(gui_for_word_input())
lost_letters=[]
general_gui(word,lost_letters)