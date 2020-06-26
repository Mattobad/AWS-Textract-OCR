import boto3
import json
import sys
import re
#from trp import Document
import trp 
import helper_func as hp



def lambda_handler(event,context):

	# Amazon Textract
	textract = boto3.client(
		service_name = 'textract',
		region_name = 'us-east-1'
		)

	# Amazon s3
	s3 = boto3.client('s3')

	try:
		obj = event["Records"][0]["s3"]
		bucket = str(obj["bucket"]["name"])
		file_name = str(obj["object"]["key"])
		file_name_final = file_name.split(".")
		# AWS textract being from here
		response =textract.analyze_document(
			Document={
				'S3Object': {
					'Bucket':bucket,
					'Name': file_name
				}
			},
			FeatureTypes=['TABLES','FORMS'])

		#calling textract parser module
		doc = trp.Document(response)
		#table_content = []
		line_content = []
		content_table = []
		content_form = []
		#Looping through doc response
		for page in doc.pages:

			for line in page.lines:
				#line_content += (line.text) + "\n"
				line_content.append(line.text)
			
			#for forms
			forms = hp.outputForm(page)

			for items in forms:
					#content += '\n'
				for item in items:
						#content +=item 
					content_form.append(item)
				
			# for tables
			content_table= hp.outputTable(page)
			
		# removing duplicates
		for line in line_content:
			#print("line value => ",line)
			for item in content_table:
			 	#print("item value before => ",item)

			 	if line in item:
			 		#print("line after delete => ",line)
			 		line_index = line_content.index(line)
			 		line_content[line_index] = "table"
			 		break

		#final removable of duplicates
		final_line_list = hp.Remove(line_content)
		for item in final_line_list:
			if "table" in item:
				final_line_list.remove("table")

		# copying the list elements into text
		content =""
		for item in final_line_list:

			content += item + ' '

		for items in content_table:
				#print('')
			content += '\n'
			for item in items:
				content += item + '\t'

		#uploading the file into the bucket
		s3.put_object(Bucket=bucket, Key="text_files/{}.txt".format(file_name_final[0]),Body=content)

	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

		










