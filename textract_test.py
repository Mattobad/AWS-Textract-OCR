import boto3
import json
import sys
#from trp import Document
import trp 

# Amazon Textract
textract = boto3.client(
	service_name = 'textract',
	region_name = 'us-east-1')


# Amazon s3
s3 = boto3.resource('s3')


# function for table....
def outputTable(page):
	csvData = []
	#print("/////////////////////////////")
	for table in page.tables:
		csvRow = []
		csvRow.append("Table")
		csvData.append(csvRow)
		for row in table.rows: 
			csvRow = []
			for cell in row.cells:
				csvRow.append(cell.text)
			csvData.append(csvRow)
		csvData.append([])
		csvData.append([])

	return csvData

file_name = str(sys.argv[1])
# try:
response =textract.analyze_document(
	Document={
		'S3Object': {
			'Bucket':'your_bucket_name',
			#'Name':str(sys.argv[1])
			'Name' : file_name
		}
	},
	FeatureTypes=['TABLES','FORMS'])


print('')




doc = trp.Document(response)
content =''
for page in doc.pages:
	table = outputTable(page)
	for items in table:
		#print('')
		content += '\n'
		for item in items:
			content += item + '\t'

			#print(item,'\t',end=' ')
	#forms = outputForm(page)
s3.Object('your_bucket_name',file_name+'.txt').put(Body=content)



#print(table)