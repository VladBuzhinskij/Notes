import model
import View
class Controller:
    view=View.View()
    model=model.Note()

    def __init__(self):
         print("")
    def run(self):
        
        cycle=True
        while(cycle):
            self.view.com()
            input=self.view.inputData()
            match input:
                case "New" :
                    inp=self.view.createNote()
                    self.model.add(inp[0],inp[1])
                case "Print":
                    self.view.printArr(self.model.readListHead())
                case "Note":
                    self.view.printNote(self.model.readNote(self.view.inputNumber()))
                case "Edit":
                    edit=self.view.editNote()
                    self.model.editNote(edit[0],edit[1],edit[2])
                case "Del":
                    self.model.deliteNote(self.view.inputNumber())
                case "Exit":
                    cycle=False
            