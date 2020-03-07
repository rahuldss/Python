import pandas as pd

file = pd.ExcelFile("/Users/narendersharma/Downloads/GICDues.xlsx")
print(file.sheet_names)

sheet = file.parse('sheet1')
print(sheet)
print(type(sheet))

print(sheet.Sno)    # Column Name

print(sheet.Amount.sum())    # Column - Sum

print(sheet.loc[0]) # first row

print(sheet.loc[0, "Amount"]) # first row's column

sheet.set_index("sheet1", inplace=True) # Set Filter

sheet.loc[ sheet["Amount"] > 2000 ] # Amount > 2000

sheet.loc[ sheet["Amount"].idxmax() ] # Max Amount

sheet.loc[ sheet["Amount"].idxmax() ]["Customer"] # Max Amount's Column Value

sheet.loc[ sheet["Amount"] > 2000 ]["Customer"].unique() # Unique

sheet.loc[ sheet["Amount"] > 2000 ]["Customer"].unique()[0] # First out of Uniques

for customer in sheet.loc[ sheet["Amount"] > 2000 ]["Customer"].unique():
    print(customer)
