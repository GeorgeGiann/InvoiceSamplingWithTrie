
class Trie:

    def __init__(self):
	"""
	Trie node constructor function
   
	"""
	self.children = {} #parent directory pointing to existing children
	self.Infos = None  #Storing variable for nodes info -- not used
	"""
	Flag value stating if the node is an ending node with True, or 
	an intermediate node, with False
	"""
	self.store_node = False 
	self.listed_values = [] #Storing list -- not used 

#end of constructor declaration

    
    def addNode(self, key):
	"""
	Add a new node in the trie, by calling this function recursively.
	Takes the first char from key and checks if there is a branch for this
	char. If there is, goes to next key char, if not a new node is created
	until it passes all key chars.  

	Args:
	    key: string key indexing trie node
	"""   
	head = key[0]
	if head in self.children:
	    node = self.children[head]
	else:
	    node = Trie()
	    self.children[head] = node

	if len(key) > 1:
	    remaining_key = key[1:]
	    node.addNode(remaining_key)
	else:
	    node.store_node = True

#end of addNode declaration

    def getNode(self, key):

	"""
	Retrieve Trie node's validation value
	If True node is a final node that has previosly
	been created and corresponds to a key(code)
	If False, there is not a node that correspond
	to this key 

	Args:
	    key: string key indexing trie node 
	"""

	head = key[0]
	if head in self.children:
	    node = self.children[head]
	else:
	    return False


	if len(key) > 1 :
	    remaining_key = key[1:]
	    return node.getNode(remaining_key)
	elif node.store_node :
	    return node.store_node
	else:
	    return False
#end of getNode declaration

  



    
