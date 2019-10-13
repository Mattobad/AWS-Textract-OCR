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

# try:
response =textract.analyze_document(
	Document={
		'S3Object': {
			'Bucket':'your_bucker_name',
			'Name':str(sys.argv[1])
		}
	},
	FeatureTypes=['TABLES','FORMS'])


print('')

doc = trp.Document(response)

# obj_page = trp.Page()
# lines = obj_page.getLinesInReadingOrder()

# for line in lines:
# 	print(line)
#def multi_list_func()
col_index =0
str_line =''
for page in doc.pages:
	#print tables
	#print(page.getLinesInReadingOrder)
	for table in page.tables:
		# print(len(table.rows))
		# print(len(table.rows.cells))
		#print(len(table.columns))
		for r, row in enumerate(table.rows):
			#print(r,row)
			#print('after row')
			colmn = len(row.cells)
			for c, cell in enumerate(row.cells):

				#print('{} {} {}'.format(r,c,cell.text))
				if col_index < colmn:
					#print(r,c,col_index,colmn)
					str_line += cell.text
					col_index +=1
				else:
					print(str_line,'\n')
					file = open("myText.txt","a")
					file.write(str_line)
					file.close()
					col_index = 0
					str_line =''
					



# except Exception as e:
# 	print(e.message)