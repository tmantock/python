from xlrd import open_workbook

wb = open_workbook('filename.ext')

data = []

for sheet in wb.sheets():
  number_of_rows = shee.nrows
  number_of_columns = sheet.ncols
  
  for row in range(number_of_rows):
    # Add values to this array
    sub = []
    
    # Loop over each column in the row and add data to the dictionary
    for col in range(number_of_columns):
      value = str((sheet.cell(row, col).value))
      sub.append(value)
    
    # Append sub array to data array to create a multi-dimensioanl array
    data.append(sub)
    
    # Alternatively, you can do something with the data here instead of appending
    # Access data like item["name"]
    
for item in data:
  # Do something with data
  
  # Get data from data array like item["name"]
  
