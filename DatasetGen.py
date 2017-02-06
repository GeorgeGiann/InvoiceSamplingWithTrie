import random
import time

"""
Files creation and initialization 
"""

#create and initialise with colomn names 'customer.csv' file
customer = open('customer.csv','w')
customer.write("\"CUSTOMER_CODE\",\"FIRSTNAME\",\"LASTNAME\"\n")

#create and initialise with colomn names 'invoice.csv' file
invoice = open('invoice.csv','w')
invoice.write('\"CUSTOMER_CODE\",\"INVOICE_CODE\",\"AMOUNT\",\"DATE\"\n')

#create and initialise with colomn names 'invoice_item.csv' file
invoice_item = open('invoice_item.csv','w')
invoice_item.write('\"INVOICE_CODE\",\"ITEM_CODE\",\"AMOUNT\",\"QUANTITY\"\n')

customer_sample = open('customer_sample.csv','w')
customer_sample.write("\"CUSTOMER_CODE\"\n")

"""
Parameters declaration and initialization
"""
#Number rows in customer.csv
NumOfUniqueCodes = 500000 
#Number of rows in invoice.csv
NumOfInvoices = 2 * NumOfUniqueCodes
#Number of rows in invoice_item.csv  
NumOfItem = 5 * NumOfInvoices
#Number of customer_samples.csv
NumOfSamples = 1000

data = range(1,NumOfUniqueCodes)
random.shuffle(data)
samples = data[0:NumOfSamples-1]

#Helping variables declaration
CodePrefix = 'CUST0000000000'
InvoicePrefix = 'INV0000000'
stime=time.mktime(time.strptime('1-Jan-2001','%d-%b-%Y'))
inc = 50000 


"""
arguments(type): invcode(string) invoice code, 
amount(float) , 
div(int between 1 - 9) number of discrete items
Function: writes in invoice_items.csv under the assumption that dicrete 
items amount is equally divided
"""
def write_items(invcode, amount, div):
    piece = round(amount/div)
    for i in range(1,div+1):
	line = '\"'
	line+= invcode
	#No need to know what the item really is
	item = 'ITEM'+str(random.randint(1,100)) + '\",\"'
	line += item
	line += (str(piece)+'\",\"')
	quantity = str(random.randint(1,100)) + '\"\n'
	line +=quantity
	invoice_item.write(line)
	


#loop that writes customer.csv
for i in range(1,NumOfUniqueCodes+1) :
    line = '\"'
    codeNum = str(i)
    code = CodePrefix[0:-len(codeNum)] + codeNum + '\",\"'
    line+=code
    #no need to know real names
    fname='FIRST'+str(i)+'\",\"'
    line+=fname
    lname = 'LAST'+str(i)+'\"\n'
    line+=lname
    customer.write(line)


#loop that writes invoice.csv and invoice_item
for j in range(1,NumOfInvoices):
    line = '\"'
    custNum = str(random.randint(1,NumOfUniqueCodes)) 
    custCode = CodePrefix[0:-len(custNum)] + custNum + '\",\"'
    line+=custCode
    invNum = str(j)
    invCode = InvoicePrefix[0:-len(invNum)] + invNum +'\",\"'
    line+=invCode
    amount = float("{0:.2f}".format(random.uniform(70,120)))
    amountstr = str(amount) +'\",\"'
    line +=amountstr
    #function call writes invoice_item.csv
    write_items(invCode, amount, random.randint(1,9))
    stime += random.randint(0,2)*inc
    date = str(time.strftime('%d-%b-%Y',time.localtime(stime))) + '\"\n'
    line+=date
    invoice.write(line)
    
for ind in samples: 
    codeNum = str(ind)
    code = '\"'+CodePrefix[0:-len(codeNum)] + codeNum + '\"\n'
    customer_sample.write(code)
	



