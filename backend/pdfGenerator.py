from fpdf import FPDF

def generate_pdf(text: str, path: str = "output.pdf") -> None:
    txt = text.encode('latin-1', 'replace').decode('latin-1')
    pdf = FPDF()
    pdf.set_margins(20, 15, 20)
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, txt=txt, border=0, align='J')
    pdf.output(path) # pdf.output(dest='S').encode('latin-1')
    return None
