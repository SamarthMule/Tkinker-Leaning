from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="Info Message Box",message="You are a person")
    # messagebox.showwarning(title="Warning Message Box",message="You have a VIRUS!!!")
    # messagebox.showerror(title="Error Message Box", message="Something Went Wrong")
    # if messagebox.askokcancel(title="Ask ok Cancel", message="Do you want to do thing ?"):
    #     print("You Did a Thing")
    # else:
    #     print("You Cancel a Thing")
    # if messagebox.askretrycancel(title="Ask Retry Cancel",message="Do you want to retry the thing"):
    #     print("You retried a thing")
    # else:
    #     print("You cancel a thing")
    # if messagebox.askyesno(title="Ask You No", message="Do you like cake?"):
    #     print("I like cake too :)")
    # else:
    #     print("Why do you not like cake ? :(")
    # answer = messagebox.askquestion(title="Ask Question",message="Do you like pie")
    # if answer == 'yes':
    #     print("I like pie too !!")
    # else:
    #     print("Why do you not like pie ? ")
    answer = messagebox.askyesnocancel(title="Ask Yes No Cancel",
                                       message="Do you like to code ?")  # icon='warring' || icon='error' || icon='info'
    if answer == TRUE:
        print("You like to code :)")
    elif answer == FALSE:
        print("Why Not ?")
    else:
        print("You dodged the question!")


window = Tk()

button = Button(window, command=click, text='Click Me')
button.pack()

window.mainloop()
