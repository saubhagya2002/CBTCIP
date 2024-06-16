from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph # type: ignore
from reportlab.lib.styles import getSampleStyleSheet # type: ignore
from reportlab.lib import colors # type: ignore
from datetime import datetime

def generate_receipt(customer_name, items, total_cost, file_name):
    # Create a list of data for the table
    data = [["Item", "Quantity", "Price", "Total"]]
    for item in items:
        name, quantity, price = item
        total = quantity * price
        data.append([name, str(quantity), f"Rs {price:.2f}", f"Rs {total:.2f}"])

    # Add a row for the total cost
    data.append(["", "", "", f"Total: Rs {total_cost:.2f}"])

    # Create a PDF document
    doc = SimpleDocTemplate(file_name, pagesize=letter)

    # Get the default style sheet
    styles = getSampleStyleSheet()

    # Create a table from the data
    table = Table(data)

    # Apply some basic styling to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 14),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, -1), (-1, -1), colors.grey),
                        ('TEXTCOLOR', (0, -1), (-1, -1), colors.whitesmoke),
                        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, -1), (-1, -1), 14)])

    table.setStyle(style)

    # Add the table to the document
    elements = []
    elements.append(table)

    # Add customer name and receipt title
    elements.insert(0, Paragraph(f"Receipt for {customer_name}", styles["BodyText"]))
    elements.insert(1, Paragraph("", styles["BodyText"]))  # Add a blank line
    elements.insert(2, Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["BodyText"]))

    # Build the PDF document
    doc.build(elements)
    print(f"Receipt saved as {file_name}")

# Example usage
customer_name = "Saubhagya"
items = [
    ("Product A", 2, 9.99),
    ("Product B", 1, 14.99),
    ("Product C", 3, 5.99)
]
total_cost = sum(qty * price for _, qty, price in items)
file_name = "receipt2.pdf"

generate_receipt(customer_name, items, total_cost, file_name)