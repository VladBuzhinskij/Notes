# идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки
# сохранением, чтением,
# добавлением, редактированием и удалением заметок
import csv
import datetime


class Note:
    __listNotes = []

    def __init__(self):
        self.__read()

    def __read(self):
        with open("note.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            count = 0
            for row in file_reader:
                self.__listNotes.append(row)

    @classmethod
    def __write(self):
        with open("note.csv", mode="w", encoding='utf-8') as w_file:
            file_writer = csv.writer(
                w_file, delimiter=";", lineterminator="\r")
            for row in self.__listNotes:
                file_writer.writerow(row)

    def add(self, head, body):
        id = int((self.__listNotes[-1])[0])+1
        self.__listNotes.pop(-1)
        today = datetime.datetime.today()
        date = today.strftime("%Y.%m.%d  %H:%M:%S")
        self.__listNotes.insert(0,[str(id), head, body, date])
        self.__listNotes.append([str(id),0])
        Note.__write()

    def readListHead(self):
        resList = []
        for number in range(len(self.__listNotes)-1):
            resList.append((self.__listNotes[number])[:2])
            resList[number].append((self.__listNotes[number])[3])
        return resList
    
    def readNote(self,id):
        for row in self.__listNotes:
            if id==int(row[0]):
                return row
        print("Заметка не найдена")

    def editNote(self,id,head,body):
        today = datetime.datetime.today()
        date = today.strftime("%Y.%m.%d  %H:%M:%S")
        note=False
        for number in range(len(self.__listNotes)-1):
            if int(id)==int(self.__listNotes[number][0]):
                self.__listNotes[number][1]=head
                self.__listNotes[number][2]=body
                self.__listNotes[number][3]=date
                self.__listNotes.insert(0,self.__listNotes[number])
                self.__listNotes.pop(number+1)
                note=True
        if note:
            Note.__write()
        else: print("Заметка не найдена")

    def deliteNote(self, id):
        note=False
        for number in range(len(self.__listNotes)-1):
            if id==int(self.__listNotes[number][0]):
                self.__listNotes.pop(number)
                note=True
        if note:
            Note.__write()
        else: print("Заметка не найдена")
    