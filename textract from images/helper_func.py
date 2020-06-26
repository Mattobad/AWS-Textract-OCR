
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

def two_columns(response):

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
		 	#print(finalLine)
		 	return finalLine
		#print(line[line[0 in line or 1 in line]])
	# except Exception as e:
	# 	print(e.message)
