import sys.re
from handlers import *
from util import *
from rules import *
class Praser:
	def __init__(self,handler):
		self.handler=handler
		self.rules=[]
		self.filters=[]
	def addRule(self,rule):
		self.rules.append(rule)
	def addFileter(self,pattern,name):
		def filter(block,handler):
			return re.sub(pattern,handler,sub(name),block)
		self.filter.append(filter)
	def parse(self,file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters::
				block=filter(block,self.hander)
			for rule in self.rules:
				if rule.condition(block):
					lase=rule.action(block,self.handler)
					if last:break
		self.handler.end('document')
class BasicTextParser(Parser):
	def __init__(self,handler):
		parser.__init__(self,handler)
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadingRule())
		self.addRule(ParagraphRule())
		self.addFilter(r'\*(.+?)\*','emphasis')
		self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
		self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')
hander=HTMLRender()
praser=BasicTextParser(handler)
parser.parse(sys.stdin)



