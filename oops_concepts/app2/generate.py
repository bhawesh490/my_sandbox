from fpdf import FPDF

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as theri names,their due amount
    and the period of the bill 
    """ 

    def __init__(self,filename):
        self.filename=filename

    def generate(self,flatmate1,flatmate2,bill):
        pdf=FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()
        # add the title
        pdf.set_font(family='Times',size=24,style='B')
        pdf.cell(w=0,h=80,txt='Flatmate Bills',border=1,align="c",ln=1)

        # Insert Period labels and values
        pdf.cell(w=100,h=40,txt='Period',border=1)
        pdf.cell(w=150,h=40,txt=bill.period,border=1,ln=1)
        
        # Insert Name and bill of the first flatmate
        pdf.cell(w=100,h=40,txt=flatmate1.name,border=1)
        pdf.cell(w=150,h=40,txt=str(flatmate1.pays(bill,flatmate2)),border=1,ln=1)
        
        pdf.output(self.filename)
