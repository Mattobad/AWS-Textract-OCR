import boto3
import json
import sys
from pprint import pprint

# Amazon Textract
textract = boto3.client(
	service_name = 'textract',
	region_name = 'us-east-1')


# Amazon s3
s3 = boto3.resource('s3')

try:
	response =textract.detect_document_text(
		Document={
			'S3Object': {
				'Bucket':'your_bucket_name',
				'Name':str(sys.argv[1])
			}
		}
	)

	#pprint(response)

	print('')

	for item in response['Blocks']:
		if item['BlockType'] == "LINE":
			print(item["Text"])

	print('')

except Exception as e:
	print(e.message)


