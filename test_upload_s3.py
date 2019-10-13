import boto3
import os
# Amazon s3
s3 = boto3.resource('s3')

content ="Testing for putting text file in s3 bucket"

s3.Object('your_bucket_name','test_text.txt').put(Body=content)

#test_textract_file
# for subdir,dirs,files in os.walk('/test_textract_file'):
# 	for file in fiels:
# 		full_path = os.path.join(subdir,file)
# 		bucket.put_object(Key='/test_textract_file'+full_path[len(path)+1:],Body=content)