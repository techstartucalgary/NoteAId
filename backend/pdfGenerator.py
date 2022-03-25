from fpdf import FPDF

def pdfGenerator(text: str, fileName: str = "PDFOutput") -> None:
    txt = text.encode('latin-1', 'replace').decode('latin-1')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, txt=txt, border=0, align='L')
    pdf.output(f'{fileName}.pdf')
    return None
