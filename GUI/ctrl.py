from Comp import Comp
import tkinter as tk

class Ctrl():

	listOfComp = []

	@staticmethod
	def openfile(e=None):
		from gui import Gui
		filename = Gui.exploreFile()
		if e!=None:
			Gui.setText(e, filename)

	@staticmethod
	def emptyText(e):
		e.delete(0,tk.END)	

	@staticmethod
	def setText(e, text):
		Ctrl.emptyText(e)
		e.insert(0, text)
		return		

	@staticmethod
	def checkSub(top, e, list):
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			Gui.addElToList(list, (e[0].get(),e[1].get()))
			Gui.destroyTop(top)

	@staticmethod
	def checkComp(top, e, l, list):
		comp = Comp()
		if len(e[0].get()) != 0 and len(e[1].get()) != 0:
			from gui import Gui
			comp.setName(e[0].get())
			comp.setPath(e[1].get())
			for t in l[0].get(0,l[0].size()):
				comp.addOpt1(t)
			for t in l[1].get(0,l[1].size()):
				comp.addOpt2(t)
			Ctrl.listOfComp.append(comp)		
			Gui.addElToList(list, str(comp))
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

