# AWS-Textract
Extraction of text from images on Amazon S3 bucket using Amazon Textract API. Note: "trp" stands for "Textract Response Parser" modules.

### textract from images:
  - AWS lambda function which serves as OCR(Optical Character Recognition) leveraging the power of Amazon textract to extract the text from the images uploaded on S3(Simple Storage Service) bucket. So, whenever the image is uploaded to the dedicated S3 bucket the lambda function, it gets trigger resulting in text file with all the text extracted from the images file.
  
  **Note**: Need to setup the trigger in the AWS lambda in order to execute the function.
