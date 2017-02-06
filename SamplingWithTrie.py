from Trie import Trie
import csv


#open costumer_sample.csv file in order to read its content
sample_file = open('customer_sample.csv')
samples = csv.reader(sample_file)

#create two Tries to find the rows needed according to samples 
CustomerTrie = Trie()
InvoiceTrie = Trie()


print 'Scanning sample file and creating trie'

#Create a trie for the costumer codes by accessing costumer_sample.csv
rownum = 0
for row in samples:
    if rownum == 0:
	#ingore first line (column headers)
	rownum+=1
	continue
    CustomerTrie.addNode(row[0][4:])

sample_file.close()
print 'End Scanning customer_sample.csv'

# open file customer.csv to read contents
customer_file = open('customer.csv')
customer = csv.reader(customer_file)

#create and initialise with colomn names 'new_customer.csv' file
new_customer = open('new_customer.csv','w')
new_customer.write("\"CUSTOMER_CODE\",\"FIRSTNAME\",\"LASTNAME\"\n")

print 'Scanning customer file and creating trie'


"""
Use CustomerTrie the customer codes correspond to costumer samples.
Acceess all costumer.csv rows and chech if there is a node for each
costumer code.
If there is write this row in the new file
If not continue to next rows
"""

rownum = 0
for row in customer:
    if rownum == 0:
	#ingore first line (column headers)
	rownum+=1
	continue
    if CustomerTrie.getNode(row[0].replace('CUST','')):
	new_customer.write('\"'+row[0]+'\",\"'+row[1]+'\",\"'+row[2]+'\"\n')

#close no longer needed files
customer_file.close()
new_customer.close()

print 'End Scanning customer.csv'


#open file invoice.csv to read its contents
invoice_file = open('invoice.csv')
invoice = csv.reader(invoice_file)

#create and initialise with colomn names 'new_invoice.csv' file
new_invoice = open('new_invoice.csv','w')
new_invoice.write('\"CUSTOMER_CODE\",\"INVOICE_CODE\",\"AMOUNT\",\"DATE\"\n')

print 'Scanning invoice file and creating trie'

"""
Read invoice.csv lines. Check if the customer code of every line is indexed
in CustomerTrie. 
If yes write this line in new_invoice.csv and create a new node in the 
InvoiceTrie structure.
If not proceed to next line 
"""

rownum = 0
for row in invoice:
    if rownum == 0:
	#ingore first line (column headers)
	rownum+=1
	continue
    if CustomerTrie.getNode(row[0].replace('CUST','')):
	InvoiceTrie.addNode(row[1].replace('INV',''))
	new_invoice.write('\"' +row[0]+ '\",\"' +row[1]+ '\",\"' +row[2]+ '\",\"' +row[3]+ '\"\n')
#close no longer needed files
invoice_file.close()
new_invoice.close()
print 'End Scanning invoice.csv'

#open file invoice_item.csv to read contents
items_file = open('invoice_item.csv')
items = csv.reader(items_file)

#create and initialise with colomn names 'new_invoice_item.csv' file
new_invoice_item = open('new_invoice_item.csv','w')
new_invoice_item.write('\"INVOICE_CODE\",\"ITEM_CODE\",\"AMOUNT\",\"QUANTITY\"\n')

print 'Scanning invoice_item file'

"""
Read invoice_item.csv and check if each corresponding invoice code has been
created in the CustomerTrie. 
If yes write write this line in new_invoice_item.csv.
If not proceed to next line
"""

rownum = 0
for row in items:
    if rownum == 0:
	rownum+=1
	continue
    if InvoiceTrie.getNode(row[0].replace('INV','')):
	new_invoice_item.write('\"'+row[0]+'\",\"'+row[1]+'\",\"'+row[2]+'\",\"'+row[3]+'\"\n')
items_file.close()
new_invoice_item.close()
print 'End Scanning invoice_item.csv'














