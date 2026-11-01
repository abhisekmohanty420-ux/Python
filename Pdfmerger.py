from PyPDF2 import PdfWriter


merge=PdfWriter()
pdf=[]
n=int(input("How many pdf do you want to merge"))

for i in range(0,n):
    name=input(f"Enter the name of PDF {i+1}")
    pdf.append(name)


for pd in pdf:
    merge.append(pd)

merge.write("merged-pdf.pdf")
merge.close()        


