def lines(file):
	for line in file: yield line;
	yield '/d'//在文件后面增加一空白行

def blocks(file)：
	block=[]
	for line in lines(file)
	 	  if  line.strip():#存在字符，不为空,去掉两边的空格
	 	     block.append(line)#将该行加在block末尾
	 	  elif block: #该行不存在，block存在
	 	     yield ''.join(block).strip()#返回该block，重建一个空block开始下一轮循环
	 	     block=[]
