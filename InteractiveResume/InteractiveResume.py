from Tkinter import *
import Tkinter
import tkMessageBox


#------------------------------------------------------------------------------------------------------
#InteractiveResume class is stating from here
#------------------------------------------------------------------------------------------------------
class InteractiveResume(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.Int_Resume()
        
    def Int_Resume(self):
      
           
        self.pack()
		
        Academic = Button(self, text="Academic Qualification", command=self.Academic, height=5, width=22)
        Academic.grid(row=0, column=0)
        Interest = Button(self, text="Interest", command=self.Interest, height=5, width=22)
        Interest.grid(row=0, column=1)
        Experience = Button(self, text="Experience", command=self.Experience, height=5, width=22)
        Experience.grid(row=0, column=2)
        Achievements = Button(self, text="Achievements", command=self.Achievements, height=5, width=22)
        Achievements.grid(row=0, column=3)


#Address of the files(Axademic.txt, Interest.txt, Experience.txt, Achievements.txt and contact.txt) need to be changed according to address of the files. 

    def Academic(self):
        tkMessageBox.showinfo( "Academic Qualification",  file(r"Academic.txt", "rb").read())
        
    def Interest(self):
        tkMessageBox.showinfo( "Interest",  file(r"Interest.txt", "rb").read())
        
    def Experience(self):
        tkMessageBox.showinfo( "Experience", file(r"Experience.txt", "rb").read())
        
    def Achievements(self):
        tkMessageBox.showinfo( "Achievements", file(r"Achievements.txt", "rb").read())
#------------------------------------------------------------------------------------------------------
#Functions are present out of the above class
#------------------------------------------------------------------------------------------------------
def ask_quit():
   if tkMessageBox.askokcancel("Quit", "Do you want to close this program"):
		root.destroy()
def contact():
    tkMessageBox.showinfo( "Contact",  file(r"contact.txt", "rb").read())       

#------------------------------------------------------------------------------------------------------
#Actual program is starting from here
#------------------------------------------------------------------------------------------------------
root = Tk()
root.title('Interactive Resume')
Font = ('times', 20, 'bold')
widget = Label(root, text='Hi, my name is Ankit Dubey.' "\n" 'This is my resume made in python.' "\n" 'Hope you will like it :)')
widget.config(bg='blue', fg='grey')  
widget.config(font=Font)           
widget.config(height=20, width=40)       
widget.pack()

menubar = Menu(root)
menubar.add_command(label="Contact", command=contact)
menubar.add_command(label="Quit", command=ask_quit)

root.config(menu=menubar)
	
InteractiveResume(root) #calling InteractiveResume class made above.
root.mainloop()  

#--------------------------------------------Program END-----------------------------------------------------------

