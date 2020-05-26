from comp import Comp
from configuration import Conf
import tkinter as tk

class Ctrl():


	def __init__(self):
		self.conf = Conf()
		self.listOfComp = self.conf.getComp()

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
		return

	def remFromListComp(self,l):
		if not l.curselection():
			return
		del(self.listOfComp[l.curselection()[0]])
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
		if len(inex.getOpt2()) > 0:
			for el in inex.getOpt2():
				Gui.addElToList(l[1], el)

	@staticmethod
	def checkSub(top, e, list):
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			Gui.addElToList(list, (e[0].get(),e[1].get()))
			Gui.destroyTop(top)	

	@staticmethod
	def checkOption(e, l):
		if len(e[0].get()) > 0:
			from gui import Gui
			if len(e[1].get()) > 0:
				if len(e[2].get()) > 0:
					Gui.addElToList(l, (e[0].get(), e[1].get().split(e[2].get())))
				else:
					Gui.addElToList(l, (e[0].get(), e[1].get().split(None)))
			else:
				Gui.addElToList(l, (e[0].get(),[]))
		Ctrl.emptyText(e[0])
		Ctrl.emptyText(e[1])
		Ctrl.emptyText(e[2])

	def checkComp(self, top, e, l, list):
		comp = Comp()
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			comp.setName(e[0].get())
			comp.setPath(e[1].get())

			for t in l[0].get(0,l[0].size()):
				comp.addOpt1(t)
			for t in l[1].get(0,l[1].size()):
				comp.addOpt2(t)

			self.listOfComp.append(comp)		
			Gui.addElToList(list, str(comp))
			Gui.destroyTop(top)

	def checkConf(self, e, l):
		if len(e[0].get()) == 0 or len(e[1].get()) == 0 or len(e[2].get()) == 0 or len(e[3].get()) == 0:
			return
		if len(self.listOfComp) == 0:
			return 		
		self.conf.setTemplatePath(e[0].get())
		self.conf.setPayloadPath(e[1].get())
		self.conf.setSpecialChar(e[2].get())
		self.conf.setPlaceholderPayload(e[3].get())	
		if len(e[4].get()) != 0:
			try:
				rate = float(e[4].get())
				if not(rate >= 0 and rate < 1):
					return
				self.conf.setFreq(rate)
			except ValueError:
				return

		if len(e[5].get()) != 0:
			self.conf.setOut(e[5].get())	
		if l.size() > 0:
			for s in l[0].get(0, l.size()):
				self.conf.addToSub(s)
		print(self.conf)					



	def updateComp(self, top, e, l, list, index):
		comp = Comp()
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			comp.setName(e[0].get())
			comp.setPath(e[1].get())
			for t in l[0].get(0,l[0].size()):
				comp.addOpt1(t)
			for t in l[1].get(0,l[1].size()):
				comp.addOpt2(t)
			
			self.listOfComp[index] = comp
			Gui.remFromList(list, index)		
			Gui.addElToList(list, str(comp), index)
			Gui.destroyTop(top)		

