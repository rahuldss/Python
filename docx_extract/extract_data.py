# http://15minanalytics.com/2019/04/09/extract-information-from-a-ms-word-file-using-python/

from docx import *
import re
import json

#----------01_Import File Name----------
document = Document('./Docs/APRIL 2019 IDSU & COMM RENT NOIDA.docx')  #Change filename here

#02_-----------Declare Variables-----------
bolds=[]
emails=[]
phones=[]

#-----------03_Extract Elements From the Word File-----------
for para in document.paragraphs:

    #03.1 Find email and phone numbers within the paragraph text
    text = para.text
    email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text)
    phone_list = re.findall(r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]',text)

    for email in email_list:
        emails.append(email)

    for phone in phone_list:
        for ph in phone.split():
            phones.append(ph)

    #03.2 Find the bold style within the word document
    # for run in para.runs:
    #     if run.bold :
    #         bolds.append(run.text)

#-----------04_Create Output-----------
style_Dict={'emails':emails,
              'phone_numbers':phones
            #   ,'bold_phrases':bolds
              }

print("\nWord File Output:\n")

# print(phones)

r = json.dumps(style_Dict)
loaded_r = json.loads(r)
print("\n",json.dumps(loaded_r,indent=4, sort_keys=False))  #Pretty print the JSON output
