from tkinner import Tk, Frame
class mengubahjudul(Frame):
    def_init_(self,parent):
        Frame._init_(self,parent,)
        
        self.tampilan = parent
        
        self.initUI()
        
    def initUI(self):
        self.tampilan.title("Judul Oyy")

if_name_ == '_main_' :
    root = Tk()
    app = mengubahjudul(root)
    root.mainloop()
