import boto3
import json
import sys

# Amazon Textract
textract = boto3.client(
	service_name = 'textract',
	region_name = 'us-east-1')


# Amazon s3
s3 = boto3.resource('s3')
# try:


# getting the response back from the textract
response =textract.detect_document_text(
	Document={
		'S3Object': {
			'Bucket':'your_bucket_name',
			'Name':str(sys.argv[1])
		}
	}
)


columns =[]
lines = []


for item in response["Blocks"]:
	#print("Reponse file",item.LINE)
	column_found = False
	if item["BlockType"] == "LINE":
		column_found =False
		for index, column in enumerate(columns):
			bbox_left = item["Geometry"]["BoundingBox"]["Left"]
			bbox_right=item["Geometry"]["BoundingBox"]["Left"] +item["Geometry"]["BoundingBox"]["Width"]
			bbox_centre=item["Geometry"]["BoundingBox"]["Left"] +item["Geometry"]["BoundingBox"]["Width"]/2
			column_centre = column["left"] + column["right"]/2

			if (bbox_centre> column["left"]  and bbox_centre<column["right"]) or (column_centre > bbox_left and column_centre<bbox_right):
				#Bbox appears inside the column
				lines.append([index,item["Text"]])
				column_found = True
				break

	if not column_found:
		if 'Text' in item:
			#print("Success")
			columns.append({'left': item["Geometry"]["BoundingBox"]["Left"],'right':item["Geometry"]["BoundingBox"]["Left"] + item["Geometry"]["BoundingBox"]["Width"]})
			lines.append([len(columns)-1,item["Text"]])
		# else:
		# 	print("Not working")
		


lines.sort(key=lambda x: x[0])
finalLine = []
#print(lines)
for line in lines:
	 finalLine = line[0 in line or 1 in line]
	 flag = 0 in line or 1 in line
	 if flag == True:
	 	print(finalLine)
	#print(line[line[0 in line or 1 in line]])
# except Exception as e:
# 	print(e.message)


