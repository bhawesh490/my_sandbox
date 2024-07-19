from flat import Bill,Flatmate
from generate import PdfReport        

the_bill=Bill(amount=120,period='March-2023')
bhawesh=Flatmate(name='Bhawesh',days_in_house=20)
soumya=Flatmate(name='Saumya',days_in_house=25)
print("Bhawesh Pays the bill",bhawesh.pays(bill=the_bill,flatmate2=soumya))
print("Soumya Pays the bill",soumya.pays(bill=the_bill,flatmate2=bhawesh))
pdf_report=PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=bhawesh,flatmate2=soumya,bill=the_bill)








