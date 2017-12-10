class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None 



def question5(ll, m):
	x = ll
	y = ll

	for i in range(0, m):
		if (x == None): 
			return None
		x = x.next
	while (x != None):
		x = x.next
		y = y.next
	return y.data


apple = Node("Hahaha, I like it")
banana = Node("Not for me")
orange = Node("Ah, give me more")
kiwi = Node("Uh, no thanks")
mango = Node("Huh, no way")

apple.next = banana 
banana.next = orange
orange.next = kiwi 
kiwi.next = mango

print question5(apple, 3)

