from source import PDFGenerator
import time 
from models import Account, Invoice, InvoiceItem


account_bill = Account("", "User: Vasya", "", "vasya@gmail.com")
account_ship = Account("NLO", "NLO", "", "noreply@nlo.ai")
invoice_items = [
    InvoiceItem("Data handling", 1.2, 0.32),
    InvoiceItem("AI generation", .4, 0.6),
]
invoice = Invoice(account_bill, account_ship, invoice_items, tax_rate=0.5)
test_data = {
    "invoice": invoice
}

pdf_maker = PDFGenerator("templates", "static")
pdf = pdf_maker.run("invoice_gemini.html", **test_data)
with open(f"dest/{time.time_ns()}.pdf", "wb") as _:
    _.write(pdf)
