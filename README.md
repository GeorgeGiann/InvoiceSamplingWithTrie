# InvoiceSamplingWithTrie
Pre-select 1000 customers as test sample to ensure a  speedy test automation process.  Based on this input, extract all relevant entries from the three full extraction  files to produce three smaller files containing all the pre-selected  data.

The test automation process will then ingest these smaller set of files to perform the test automation execution quickly. 

The three full extraction files, all extraction files will have the following files specification: 
 
  ASCII file (UNIX format) 
  First line of the file is the heading 
  Each field is separated by comma character “,” 
  All fields are double quoted regardless of data type (e.g. “Olivier”) 
  Thousand separator should not be use in the field with FLOAT data type 
  Decimal point “.” will be used in field with FLOAT data type as decimal mark .

 CUSTOMER.CSV (contains approximately 500k customer) 
 <i> Columns           Data Type </i> 
  CUSTOMER_CODE     CHAR(30) 
  FIRSTNAME         CHAR(100) 
  LASTNAME          CHAR(100)
  
  INVOICE.CSV (contains approximately 1 million invoices) 
  <i> Columns       Data Type</i>
  CUSTOMER_CODE     CHAR(30) 
  INVOICE_CODE      CHAR(30) 
  AMOUNT            FLOAT 
  DATE              DATE 
 
INVOICE_ITEM.CSV (contains approximately 5 million invoice items)
<i>Columns          Data Type </i>
  INVOICE_CODE      CHAR(30) 
  ITEM_CODE         CHAR(30) 
  AMOUNT            FLOAT 
  QUANTITY          INTEGER 
 



