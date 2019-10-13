import boto3
import json
import sys
import re
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
		#csvRow.append("Table")
		csvData.append(csvRow)
		for row in table.rows: 
			csvRow = []
			for cell in row.cells:
				csvRow.append(cell.text)
			csvData.append(csvRow)
		csvData.append([])
		csvData.append([])

	return csvData

#function returning form in key-value pair
def outputForm(page):
	csvData = []
	for field in page.form.fields:
		csvItem = []
		if(field.key):
			csvItem.append(field.key.text)
		else:
			csvItem.append("")
		if(field.value):
			csvItem.append(field.value.text)
		else:
			csvItem.append("")
		csvData.append(csvItem)
	return csvData

#Removing duplicates from calling line
def Remove(duplicate):
	final_list = []
	for item in duplicate:
		if item not in final_list:
			final_list.append(item)

	return final_list


# AWS textract begin from here
response =textract.analyze_document(
	Document={
		'S3Object': {
			'Bucket':'your_bucket_name',
			'Name':str(sys.argv[1])
		}
	},
	FeatureTypes=['TABLES','FORMS'])


print('')

doc = trp.Document(response)


#table_content = []
line_content = []
content_table = []
content_form = []

for page in doc.pages:

	for line in page.lines:
		#line_content += (line.text) + "\n"
		line_content.append(line.text)
	
	#for forms
	forms = outputForm(page)

	for items in forms:
			#content += '\n'
		for item in items:
				#content +=item 
			content_form.append(item)

		
	# for tables
	table = outputTable(page)
	
	for items in table:
			#print('')
		#content_table += '\n'

		for item in items:
			#content_table += item + '\t'
			content_table.append(item)



for line in line_content:
	#print("line value => ",line)
	for item in content_table:
	 	#print("item value before => ",item)

	 	if line in item:
	 		#print("line after delete => ",line)
	 		line_index = line_content.index(line)
	 		line_content[line_index] = "table"
	 		break
	 



final_line_list = Remove(line_content)
for item in final_line_list:
	if "table" in item:
		final_line_list.remove("table")

print(line_content)
print('')
print('')
print(final_line_list)
print('')
print(content_table)









