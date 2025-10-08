from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='L',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
page_width = pdf.w
page_height = pdf.h
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(0, 10, txt=row["Topic"], ln=1, align='L')
    #pdf.cell(0, 10, txt=str(row["Pages"]), ln=1, align='L')
    #pdf.line(x1=10, y1=21, x2=280, y2=21)
    pdf.ln(170)
    pdf.set_font("Arial", style='I', size=12)
    pdf.set_text_color(180,180,180)
    for y in range(20,170,10):
        pdf.line(10, y, 280, y)

    pdf.cell(0, 10, txt=row["Topic"], ln=1, align='R')
    for page in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(185)
        pdf.set_font("Arial", style='I', size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row["Topic"], ln=1, align='R')

        for y in range(0, int(page_height), 10):
            pdf.line(10, y, 280, y)
pdf.output("simple_example.pdf")
