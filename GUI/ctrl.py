from comp import Comp
from configuration import Conf
import tkinter as tk
from tkinter import messagebox

class Ctrl():


	def __init__(self):
		self.conf = Conf()
		self.listOfComp = self.conf.getComp()
		self.listOfSub = self.conf.getSub()

		self.tmpOpt1 = []
		self.tmpOpt2 = []

	@staticmethod
	def openfile(e=None):
		from gui import Gui
		filename = Gui.exploreFile()
		if e!=None:
			Ctrl.setText(e, filename)

	@staticmethod
	def emptyText(e):
		e.delete(0,tk.END)

	@staticmethod
	def setText(e, text):
		Ctrl.emptyText(e)
		e.insert(0, text)

	def remFromListComp(self,l):
		if not l.curselection():
			messagebox.showinfo("Info", "Seleziona un elemento dalla lista per eliminarlo")
			return
		del(self.listOfComp[l.curselection()[0]])
		from gui import Gui
		Gui.remFromListSelected(l)

	def remFromListSub(self,l):
		if not l.curselection():
			messagebox.showinfo("Info", "Seleziona un elemento dalla lista per eliminarlo")
			return
		del(self.listOfSub[l.curselection()[0]])
		from gui import Gui
		Gui.remFromListSelected(l)

	def remFromListOpt(self,l, index):
		if not l.curselection():
			messagebox.showinfo("Info", "Seleziona un elemento dalla lista per eliminarlo")
			return
		if index == 0	:
			del(self.tmpOpt1[l.curselection()[0]])
		else:
			del(self.tmpOpt2[l.curselection()[0]])
		from gui import Gui
		Gui.remFromListSelected(l)	

	def fillCompField(self, e, l, list):
		from gui import Gui
		inex = self.listOfComp[list.curselection()[0]]
		Ctrl.setText(e[0], inex.getName())
		Ctrl.setText(e[1], inex.getPath()) 

		if len(inex.getOpt1()) > 0:
			for el in inex.getOpt1():
				Gui.addElToList(l[0], el)
				self.tmpOpt1.append(el)
		if len(inex.getOpt2()) > 0:
			for el in inex.getOpt2():
				Gui.addElToList(l[1], el)
				self.tmpOpt2.append(el)

	def checkSub(self, top, e, list):
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			self.conf.addToSub((e[0].get(),e[1].get()))
			from gui import Gui
			Gui.addElToList(list, (e[0].get(),e[1].get()))
			Gui.destroyTop(top)
		else:
			messagebox.showerror("Error", "Entrambi i campi sono obbligatori")	

	def checkOption(self, e, l, index):
		if len(e[0].get()) > 0:
			t = None
			from gui import Gui
			if len(e[1].get()) > 0:
				if len(e[2].get()) > 0:
					t = (e[0].get(), e[1].get().split(e[2].get()))
					Gui.addElToList(l, t)
				else:
					t = (e[0].get(), e[1].get().split(None))
					Gui.addElToList(l, t)				
			else:
				t = (e[0].get(),[])
				Gui.addElToList(l, t)
			if index == 0:
				self.tmpOpt1.append(t)
			else:
				self.tmpOpt2.append(t)
		else:
			messagebox.showerror("Error", "Il nome dell'opzione è obbligatorio")		


		Ctrl.emptyText(e[0])
		Ctrl.emptyText(e[1])
		Ctrl.emptyText(e[2])

	def checkComp(self, top, e, list):
		comp = Comp()
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			comp.setName(e[0].get())
			comp.setPath(e[1].get())

			for t in self.tmpOpt1:
				comp.addOpt1(t)
			for t in self.tmpOpt2:
				comp.addOpt2(t)

			self.tmpOpt1 = []
			self.tmpOpt2 = []	

			self.listOfComp.append(comp)		
			Gui.addElToList(list, str(comp))
			Gui.destroyTop(top)

	def checkConf(self, e, l):
		if len(e[0].get()) == 0 or len(e[1].get()) == 0 or len(e[2].get()) == 0 or len(e[3].get()) == 0:
			messagebox.showerror("Error", "Compila i campi obbligatori")
			return
		if len(self.listOfComp) == 0:
			messagebox.showerror("Error", "Inserisci almeno un test di compilazione")
			return
		if len(e[6].get()) == 0:
			messagebox.showerror("Error", "Inserisci il nome con il quale desideri salvare la tua configurazione")
			return	

		self.conf.setTemplatePath(e[0].get())
		self.conf.setPayloadPath(e[1].get())
		self.conf.setSpecialChar(e[2].get())
		self.conf.setPlaceholderPayload(e[3].get())	
		if len(e[4].get()) != 0:
			try:
				rate = float(e[4].get())
				if not(rate >= 0 and rate < 1):
					messagebox.showerror("Error", "La frequenza deve essere un decimale compreso tra (0,1]")
					return
				self.conf.setFreq(rate)
			except ValueError:
				messagebox.showerror("Error", "La frequenza deve essere un decimale compreso tra (0,1]")
				return

		if len(e[5].get()) != 0:
			self.conf.setOut(e[5].get())	
		#vettore sub gestito a runtime
		
		print(str(self.conf))
		with open(e[6].get(), "w") as f:
			f.write(str(self.conf))

	def updateComp(self, top, e, list, index):
		comp = Comp()
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			comp.setName(e[0].get())
			comp.setPath(e[1].get())
			
			for t in self.tmpOpt1:
				comp.addOpt1(t)
			for t in self.tmpOpt2:
				comp.addOpt2(t)

			self.tmpOpt1 = []
			self.tmpOpt2 = []

			self.listOfComp[index] = comp
			Gui.remFromList(list, index)		
			Gui.addElToList(list, str(comp), index)
			Gui.destroyTop(top)		

