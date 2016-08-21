class Rule:
	def action(self,block,handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
	return True
class HeadingRule(Rule): #标题的规则title
	type ='heading'
	def cindition(self,block):
		return not '\n' in block and len(block)<=70 and not block[-1]==':'
class TitleRule(HeadingRule):#h1
	type='title'
	first=True
	def condition(self,block):
		if not self.first:return False
		self.first=False
		return HeadingRule.condition(self.block)
class ListItemRule(Rule):#li
	type='listitem'
	def condition(self.block):
		return block[0]=='-'
	def action(self,block,handler):
		handler.start(self.type)
		handler.feed(block[1:].strip())
		handler.end(self.type)
		return True
class ListRule(ListItemRule):#ul
	type='list'
	inside=False
	def condition(self,block):
		return True
	def action(self,block,handler):
		if not self.inside and ListItemRule.condition(self,block):
			handler.start(self.type)
			self,inside=Ture
		elif self.inside and not ListItemRule.condition(self,block):
			hander.end(self.type)
			self,inside=FFalse
			return False
class paragraphRule(Rule):
	type="paragraph"
	def condition(self,block):
		return True
	

