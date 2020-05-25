import unittest
import os
import sys

sys.path.append("../Component")

from compEngine import CompilationEngine
from manipulator import Manipulator

class ToolTest(unittest.TestCase):
	
	def test_input1(self):
		man = Manipulator("man-err1.conf.json")
		with self.assertRaises(KeyError):
			man.generateSource()

	def test_input2(self):
		man = Manipulator("man-err2.conf.json")
		with self.assertRaises(ValueError):
			man.generateSource()

	def test_input3(self):
		man = Manipulator("man-misto1.conf.json")
		man.generateSource()
		self.assertTrue(os.path.exists("out.c"))
		os.remove("out.c")

	def test_input4(self):
		man = Manipulator("man-misto2.conf.json")
		man.generateSource()
		self.assertTrue(os.path.exists("out.c"))
		os.remove("out.c")

	def test_input5(self):
		man = Manipulator("man-obbligatori1.conf.json")
		man.generateSource()
		self.assertTrue(os.path.exists("out.c"))
		os.remove("out.c")

	def test_input6(self):
		comp = CompilationEngine("com-err1.conf.json")
		with self.assertRaises(KeyError):
			comp.createExes()
		comp.clear()	

	def test_input7(self):
		comp = CompilationEngine("com-err2.conf.json")
		with self.assertRaises(KeyError):
			comp.createExes()
		comp.clear()	

	def test_input8(self):
		comp = CompilationEngine("com-misto1.conf.json")
		comp.createExes()
		self.assertTrue(os.path.exists("./gcc/hw.out"))
		comp.clear()

	def test_input9(self):
		comp = CompilationEngine("com-misto2.conf.json")
		comp.createExes()
		self.assertTrue(os.path.exists("./g++/hw2.out"))
		comp.clear()

	def test_input_10(self):
		comp = CompilationEngine("com-obbligatori1.conf.json")
		comp.createExes()
		self.assertTrue(os.path.exists("./gcc/a.out"))
		comp.clear()

	def test_input_11(self):
		man = Manipulator("integration.conf.json")
		man.generateSource()
		comp = CompilationEngine("integration.conf.json")
		comp.createExes()
		self.assertTrue(os.path.exists("./gcc/a.out"))
		comp.clear()	

if __name__ == '__main__':
	unittest.main()
		
