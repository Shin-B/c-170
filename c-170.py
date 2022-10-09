from tkinter import *
root=Tk()
root.title=("project 170")
root.geometry("600x600")


labelg3=Label(root)
labelg5=Label(root)
labelg10=Label(root)

class grade3:
    def __init__(self,English,Math):
        self.English=English
        self.Math=Math
    def percentage(self) :
        total=self.English+self.Math
        percent=(total*100)/200
        labelg3["text"]=percent


class grade5:
    def __init__(self,English,Math,Science):
        self.English=English
        self.Math=Math
        self.Science=Science
    def percentage(self) :
        total=self.English+self.Math+self.Science
        percent=(total*100)/300
        labelg5["text"]=percent
        
        
class grade10:
    def __init__(self,English,Math,Science,History):
        self.English=English
        self.Math=Math
        self.Science=Science
        self.History=History
    def percentage(self) :
        total=self.English+self.Math+self.Science+self.History
        percent=(total*100)/400
        labelg10["text"]=percent        
        
obj3=grade3(100,80)
obj5=grade5(100,80,35)
obj10=grade10(94,64,82,73)


btn1=Button(root,text="grade 3",command=obj3.percentage)
btn1.pack(padx=20,pady=20)
labelg3.pack(padx=20,pady=20)

btn2=Button(root,text="grade 5",command=obj5.percentage)
btn2.pack(padx=20,pady=20)
labelg5.pack(padx=20,pady=20)

btn3=Button(root,text="grade 10",command=obj10.percentage)
btn3.pack(padx=20,pady=20)
labelg10.pack(padx=20,pady=20)
        



































root.mainloop()