import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


def setFooter():
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=25)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.set_draw_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)
    pdf.ln(265)
    # Set the footer
    setFooter()
    for l in range(25):
        pdf.line(10, 21 + (l * 12), 200, 21 + (l * 12))

    for p in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        setFooter()
        for l in range(25):
            pdf.line(10, 21 + (l * 12), 200, 21 + (l * 12))


pdf.output("output.pdf")
