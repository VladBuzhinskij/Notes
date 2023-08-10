class View:
    def __init__(self):
        print("")
        

    def inputData(self):
        cycle=True
        while cycle:
            inputDat=input("Введите команду: ")
            if inputDat=="New" or inputDat=="Exit" or inputDat=="Print" or inputDat=="Note" or inputDat=="Edit" or inputDat=="Del":
                cycle=False
        return inputDat
    
    def createNote(self):
        inputHead=input("Введите заголовок: ")
        inputBody=input("Введите текст заметки: ")
        return inputHead, inputBody
    
    def printArr(self,arr):
        for row in arr:
            res="id="+row[0]+", Заголовок: "+row[1]+"   ||изм."+row[2]
            print(res)

    def inputNumber(self):
        inp=input("Введите id заметки: ")
        while not (inp.isdigit()):
            inp=input("Введите id заметки: ")
        return int(inp)
    
    def printNote(self,Note):
        print("id: "+Note[0])
        print("Заголовок: "+Note[1])
        print(Note[2])
        print("Дата и время изм.: "+Note[3])

    def editNote(self):
        id=input("Введите id заметки для изменения: ")
        while not (id.isdigit()):
            id=input("Введите id заметки для изменения: ")
        head=input("Введите новый заголовок: ")
        body=input("Введите новую заметку: ")
        return id, head,body
    
    def com(self):
        print("Список команд:\nNew - Создание заметки\nPrint - Показать список заметок\nNote - Открыть заметку\nEdit - Редактировать\nDel - Удалить\nExit - Закрыть")