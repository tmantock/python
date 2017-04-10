from xlrd import open_workbook

wb = open_workbook('filename.ext')

data = []

for sheet in wb.sheets():
  number_of_rows = shee.nrows
  number_of_columns = sheet.ncols
  
  for row in range(number_of_rows):
    #Empty dictionary - Key: Value pair - Ex dict = {'name': John, 'age': 50}
    # access value like dict['name']
    # set value like dict['name'] = "Jane"
    dict = {}
    
    # Loop over each column in the row and add data to the dictionary
    for col in range(number_of_columns):
      value = sheet.cell(row, col).value
      dict['headername' + str(col)] = value
    
    # Append row data
    # data will look like this as data is added to the list [{"name": John, "age": 90}, {"name": Joe, "age": 89}]
    data.append(dict)
    
    # Alternatively, you can do something with the data here instead of appending
    # Access data like item["name"]
    
for item in data:
  # Do something with data
  
  # Get data from data array like item["name"]
  
