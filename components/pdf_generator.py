from fpdf import FPDF


def generate_patient_pdf(patient):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 18)

    pdf.cell(190, 10, "Hospital AI Assistant", ln=True, align="C")

    pdf.set_font("Arial", "", 14)

    pdf.cell(190, 10, "Patient Medical Report", ln=True)

    pdf.ln(5)

    for key, value in patient.items():

        pdf.cell(80, 10, str(key), border=1)

        pdf.cell(110, 10, str(value), border=1)

        pdf.ln()

    filename = f"reports/{patient['Name']}.pdf"

    pdf.output(filename)

    return filename