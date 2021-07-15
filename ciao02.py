import openpyxl

wb=openpyxl.load_workbook("ciao02.xlsx")
ws=wb["Sheet1"]
for i in range(0,100):
   n= i+1
   if(n%3==0):
        ws.cell(1,n).value="HELLO"
wb.save("ciao02.xlsx")    
