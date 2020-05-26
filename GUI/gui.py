import tkinter as tk
from tkinter import filedialog
from tkinter import *

from ctrl import Ctrl

class Gui():


	def __init__(self):
		self.ctrl = Ctrl()

		self.window = tk.Tk()
		self.window.title("AVEvasion GUI")
		self.window.resizable(False, False) 
		self.focus = 1       

		self.home = None #panelHome
		self.second = None #panelConf

		self.switch = None
		self.tool = None
		self.conf = None

		self.__buildHead()
		self.__setTool()
		self.window.mainloop()

	def __buildHead(self):
		self.switch = tk.Frame(self.window, bg = "grey")
		self.switch.pack(fill = X)

		self.tool = tk.Button(self.switch, text = "Tool", command = lambda:self.__setTool())
		self.conf = tk.Button(self.switch, text = "Configuration", command = lambda:self.__setConf())

		self.tool.grid(row = 0, column = 0)
		self.conf.grid(row = 0, column = 1)
	

	@staticmethod
	def exploreFile():
		filename = filedialog.askopenfilename(initialdir = ".", title = "Select configuration file")
		return filename	

	@staticmethod
	def addElToList(l, tuple, index=END):
		l.insert(index, str(tuple))

	@staticmethod
	def remFromList(l, i):
		l.delete(i)

	@staticmethod
	def remFromListSelected(l):
		if not l.curselection():
			return
		Gui.remFromList(l, l.curselection()[0])	

	@staticmethod
	def destroyTop(top):
		top.destroy()
		top.update()

	def __newSub(self, list):
		entryArr = []

		newSub = tk.Toplevel(self.window)
		newSub.geometry("300x100+700+500")
		newSub.title("Aggiungi Sostituzione")
		labelPl = tk.Label(newSub, text = "Segnaposto", pady = 5)
		entryPl = tk.Entry(newSub)
		entryArr.append(entryPl)
		labelStr = tk.Label(newSub, text = "Stringa", pady = 5)
		entryStr = tk.Entry(newSub)
		entryArr.append(entryStr)
		btnSubmit = tk.Button(newSub, pady = 5, text = "Crea",
									 command = lambda:Ctrl.checkSub(newSub, entryArr, list))

		labelPl.grid(row = 0, column = 0)
		entryPl.grid(row = 0, column = 1)
		labelStr.grid(row = 1, column = 0)
		entryStr.grid(row = 1, column = 1)
		btnSubmit.grid(row = 2) 		

	def __updateComp(self, list):
		
		if not list.curselection():
			return

		index = list.curselection()[0]	

		entryArr = []
		listList = []
		entryOpt = []	

		newComp = tk.Toplevel(self.window)
		newComp.geometry("550x450+600+350")
		newComp.title("Modifica Compilazione")
		labelName = tk.Label(newComp, text = "Nome test", pady = 5)
		entryName = tk.Entry(newComp)
		entryArr.append(entryName)#
		labelPath = tk.Label(newComp, text = "Path compilatore", pady = 5)
		entryPath = tk.Entry(newComp)
		entryArr.append(entryPath)#
		btnPath = tk.Button(newComp, text = "Sfoglia", command = lambda:Ctrl.openfile(entryPath))
		labelOpt1 = tk.Label(newComp, text = "Opzioni Precedenti")
		listOpt1 = tk.Listbox(newComp)
		listList.append(listOpt1)#
		labelOpt2 = tk.Label(newComp, text = "Opzioni Successive")
		listOpt2 = tk.Listbox(newComp)
		listList.append(listOpt2)#
		labelOptName = tk.Label(newComp, text = "Nome Opzione", pady = 5)
		entryOptName = tk.Entry(newComp)
		entryOpt.append(entryOptName)
		labelOptValue = tk.Label(newComp, text = "Valori", pady = 5)
		entryOptValue = tk.Entry(newComp)
		entryOpt.append(entryOptValue)
		labelSeparator = tk.Label(newComp, text = "Separatore", pady = 5)
		entrySeparator = tk.Entry(newComp, width = 5)
		entryOpt.append(entrySeparator)
		btnAddOpt1 = tk.Button(newComp, text = "Aggiungi a lista P.", command = lambda:Ctrl.checkOption(entryOpt, listOpt1))
		btnAddOpt2 = tk.Button(newComp, text = "Aggiungi a lista S.", command = lambda:Ctrl.checkOption(entryOpt, listOpt2)) 
		btnRemOpt1 = tk.Button(newComp, text = "Rimuovi da lista P.", command = lambda:Gui.remFromListSelected(listOpt1))
		btnRemOpt2 = tk.Button(newComp, text = "Rimuovi da lista S.", command = lambda:Gui.remFromListSelected(listOpt2))
		btnSubmit = tk.Button(newComp, text = "Aggiorna test di compilazione", 
										pady = 10,
										command = lambda:self.ctrl.updateComp(newComp, entryArr, listList, list, index))

		self.ctrl.fillCompField(entryArr, listList, list)

		labelName.grid(row = 0, column = 0)
		entryName.grid(row = 0, column = 1)
		labelPath.grid(row = 1, column = 0)
		entryPath.grid(row = 1, column = 1)
		btnPath.grid(row = 1, column = 2)
		labelOpt1.grid(row = 2, column = 0)
		labelOpt2.grid(row = 2, column = 1)
		listOpt1.grid(row = 3, column = 0)
		listOpt2.grid(row = 3, column = 1)
		labelOptName.grid(row = 4, column = 0)
		entryOptName.grid(row = 4, column = 1)
		labelOptValue.grid(row = 5, column = 0)
		entryOptValue.grid(row = 5, column = 1)
		labelSeparator.grid(row = 5, column = 2)
		entrySeparator.grid(row = 5, column = 3)
		btnAddOpt1.grid(row = 6, column = 0)
		btnAddOpt2.grid(row = 6, column = 1)
		btnRemOpt1.grid(row = 7, column = 0)
		btnRemOpt2.grid(row = 7, column = 1)
		btnSubmit.grid(row = 8, column = 0)

	def __newComp(self, list):
		entryArr = []
		listList = []
		entryOpt = []

		newComp = tk.Toplevel(self.window)
		newComp.geometry("550x450+600+350")
		newComp.title("Aggiungi Compilazione")
		labelName = tk.Label(newComp, text = "Nome test", pady = 5)
		entryName = tk.Entry(newComp)
		entryArr.append(entryName)#
		labelPath = tk.Label(newComp, text = "Path compilatore", pady = 5)
		entryPath = tk.Entry(newComp)
		entryArr.append(entryPath)#
		btnPath = tk.Button(newComp, text = "Sfoglia", command = lambda:Ctrl.openfile(entryPath))
		labelOpt1 = tk.Label(newComp, text = "Opzioni Precedenti")
		listOpt1 = tk.Listbox(newComp)
		listList.append(listOpt1)#
		labelOpt2 = tk.Label(newComp, text = "Opzioni Successive")
		listOpt2 = tk.Listbox(newComp)
		listList.append(listOpt2)#
		labelOptName = tk.Label(newComp, text = "Nome Opzione", pady = 5)
		entryOptName = tk.Entry(newComp)
		entryOpt.append(entryOptName)
		labelOptValue = tk.Label(newComp, text = "Valori", pady = 5)
		entryOptValue = tk.Entry(newComp)
		entryOpt.append(entryOptValue)
		labelSeparator = tk.Label(newComp, text = "Separatore", pady = 5)
		entrySeparator = tk.Entry(newComp, width = 5)
		entryOpt.append(entrySeparator)
		btnAddOpt1 = tk.Button(newComp, text = "Aggiungi a lista P.", command = lambda:Ctrl.checkOption(entryOpt, listOpt1))
		btnAddOpt2 = tk.Button(newComp, text = "Aggiungi a lista S.", command = lambda:Ctrl.checkOption(entryOpt, listOpt2)) 
		btnRemOpt1 = tk.Button(newComp, text = "Rimuovi da lista P.", command = lambda:Gui.remFromListSelected(listOpt1))
		btnRemOpt2 = tk.Button(newComp, text = "Rimuovi da lista S.", command = lambda:Gui.remFromListSelected(listOpt2))
		btnSubmit = tk.Button(newComp, text = "Aggiungi test di compilazione", 
										pady = 10,
										command = lambda:self.ctrl.checkComp(newComp, entryArr, listList, list))

		labelName.grid(row = 0, column = 0)
		entryName.grid(row = 0, column = 1)
		labelPath.grid(row = 1, column = 0)
		entryPath.grid(row = 1, column = 1)
		btnPath.grid(row = 1, column = 2)
		labelOpt1.grid(row = 2, column = 0)
		labelOpt2.grid(row = 2, column = 1)
		listOpt1.grid(row = 3, column = 0)
		listOpt2.grid(row = 3, column = 1)
		labelOptName.grid(row = 4, column = 0)
		entryOptName.grid(row = 4, column = 1)
		labelOptValue.grid(row = 5, column = 0)
		entryOptValue.grid(row = 5, column = 1)
		labelSeparator.grid(row = 5, column = 2)
		entrySeparator.grid(row = 5, column = 3)
		btnAddOpt1.grid(row = 6, column = 0)
		btnAddOpt2.grid(row = 6, column = 1)
		btnRemOpt1.grid(row = 7, column = 0)
		btnRemOpt2.grid(row = 7, column = 1)
		btnSubmit.grid(row = 8, column = 0)

	def __setTool(self):
		if self.focus == 0:
			return
		else:
			self.focus = 0	

		self.window.geometry("600x250+300+200")
		if self.second != None:
			self.second.pack_forget()

		#
		self.home = tk.Frame(self.window)
		path = tk.Entry(self.home)
		sfoglia = tk.Button(self.home, text = "Sfoglia",  command = lambda:Ctrl.openfile(path))
		run = tk.Button(self.home, text = "Run")
		#
		self.home.pack(fill = BOTH, expand = 1, pady = 50)
		path.pack(pady = 5, padx = 20, fill= X)
		sfoglia.pack(pady = 5)
		run.pack(pady = 5, ipady = 5, fill = X)

	def __setConf(self):
		if self.focus == 1:
			return
		else:
			self.focus = 1


		self.window.geometry("1300x600+300+200")
		if self.home != None:
			self.home.pack_forget()

		self.second = tk.Frame(self.window)
		self.second.pack(fill = BOTH, expand = 1, pady = 25)
		self.__buildLeft()
		self.__buildRight()


	def __buildLeft(self):
		es = []

		left = tk.Frame(self.second)
		labelMan = tk.Label(left, text = "Manipulations", font="Helvetica 13 bold")
		labelTemp = tk.Label(left, text = "Template path", pady = 5)
		entryTemp = tk.Entry(left)
		es.append(entryTemp)
		btnSfoglia = tk.Button(left, text = "Sfoglia", command = lambda:Ctrl.openfile(entryTemp))
		labelPPath = tk.Label(left, text = "Payload path", pady = 5)
		entryPPath = tk.Entry(left)
		es.append(entryPPath)
		btnSfogliaPPath = tk.Button(left, text = "Sfoglia", command = lambda:Ctrl.openfile(entryPPath))
		labelSC = tk.Label(left, text = "Carattere spaciale", pady = 5)
		entrySC = tk.Entry(left)
		es.append(entrySC)
		labelPlace = tk.Label(left, text = "Segnaposto payload", pady = 5)
		entryPlace = tk.Entry(left)
		es.append(entryPlace)
		labelRate = tk.Label(left, text = "Frequenza", pady = 5)
		entryRate = tk.Entry(left)
		es.append(entryRate)
		labelOut = tk.Label(left, text = "Nome output", pady = 5)
		entryOut = tk.Entry(left)
		es.append(entryOut)
		labelSub = tk.Label(left, text = "Sostituzioni", pady = 5)
		listSub = tk.Listbox(left)
		doppioBtn = tk.Frame(left)
		btnAddSub = tk.Button(doppioBtn, text = "Aggiungi Sostituzione", command = lambda:self.__newSub(listSub))
		btnRemSub = tk.Button(doppioBtn, text = "Rimuovi", command = lambda:Gui.remFromListSelected(listSub))	

		btnS = tk.Button(left, text = "Salva Configurazione", font="Helvetica 15 bold", command = lambda:self.ctrl.checkConf(es, listSub))

		left.pack(side = LEFT)
		labelMan.grid(row = 0, column = 0)

		labelTemp.grid(row = 1, column = 0)
		entryTemp.grid(row = 1, column = 1)
		btnSfoglia.grid(row = 1, column = 2)

		labelPPath.grid(row = 2, column = 0)
		entryPPath.grid(row = 2, column = 1)
		btnSfogliaPPath.grid(row = 2, column = 2)

		labelSC.grid(row = 3, column = 0)
		entrySC.grid(row = 3, column = 1)
		
		labelPlace.grid(row = 4, column = 0)
		entryPlace.grid(row = 4, column = 1)

		labelRate.grid(row = 5, column = 0)
		entryRate.grid(row = 5, column = 1)
		
		labelOut.grid(row = 6, column = 0)
		entryOut.grid(row = 6, column = 1)

		labelSub.grid(row = 7, column = 0)
		listSub.grid(row = 7, column = 1)

		doppioBtn.grid(row = 7, column = 2)
		btnAddSub.pack()
		btnRemSub.pack()

		btnS.grid(row = 8, column = 0)

	def __buildRight(self):
		right = tk.Frame(self.second)
		labelComp = tk.Label(right, text = "Compilations", font="Helvetica 13 bold")
		labelCompList = tk.Label(right, text = "Compilazioni")
		listCompTest = tk.Listbox(right, height=20, width = 50)
		triploBtn = tk.Frame(right)
		btnAddComp = tk.Button(triploBtn, text = "Aggiungi Compilazione", command = lambda:self.__newComp(listCompTest))
		btnRemComp = tk.Button(triploBtn, text = "Rimuovi Compilazione", command = lambda:self.ctrl.remFromListComp(listCompTest))
		btnEditComp = tk.Button(triploBtn, text = "Modifica Compilazione", command = lambda:self.__updateComp(listCompTest))

		right.pack(side = RIGHT)
		labelComp.grid(row = 0, column = 0)
		labelCompList.grid(row = 1, column = 0)
		listCompTest.grid(row = 1, column = 1)
		triploBtn.grid(row = 1, column = 2)
		btnAddComp.pack()
		btnRemComp.pack()
		btnEditComp.pack()


if __name__ == "__main__":
	gui = Gui()
	



