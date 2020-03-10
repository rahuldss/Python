import pandas as pd

file = pd.ExcelFile("/Users/narendersharma/nds/Mobile EMI.xlsx")
print(file.sheet_names)

sheet = file.parse('Sheet1')
print(sheet)
print(type(sheet))

print(sheet.Oct)    # Column Name

print(sheet.Total.sum())    # Column - Sum

print(sheet.loc[0]) # first row

print(sheet.loc[0, "Total"]) # first row's column

sheet.set_index("Jan", inplace=True) # Set Filter

sheet.loc[ sheet["Total"] > 2000 ] # Total > 2000

sheet.loc[ sheet["Total"].idxmax() ] # Max Total

sheet.loc[ sheet["Total"].idxmax() ]["Jan"] # Max Total's Column Value

sheet.loc[ sheet["Total"] > 2000 ]["Jan"].unique() # Unique

sheet.loc[ sheet["Total"] > 2000 ]["Jan"].unique()[0] # First out of Uniques

for customer in sheet.loc[ sheet["Total"] > 2000 ]["Jan"].unique():
    print(customer)
