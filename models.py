# invoice.number
# invoice.date
# invoice.bill_to.company
# invoice.bill_to.name
# invoice.bill_to.address
# invoice.bill_to.email
# invoice.ship_to.company
# invoice.ship_to.name
# invoice.ship_to.address
# invoice.ship_to.email
# invoice.items
# {
#     item.description
#     item.quantity
#     item.unit_price
#     item.quantity * item.unit_price
# }
# invoice.subtotal
# invoice.tax_rate
# invoice.tax
# invoice.total

from dataclasses import dataclass
import datetime


@dataclass
class Account:
    company: str
    name: str
    address: str
    email: str

@dataclass 
class InvoiceItem:
    description: str
    quantity: float
    unit_price: float

    @property
    def value(self) -> float:
        return self.quantity * self.unit_price
    
    def __add__(self, other):
        assert isinstance(self, InvoiceItem)
        assert isinstance(other, (InvoiceItem, int, float)), TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")
        if isinstance(other, InvoiceItem) and isinstance(self, InvoiceItem):
            return  self.value + other.value

@dataclass
class Invoice:
    bill_to: Account
    ship_to: Account
    items: list[InvoiceItem]

    number: str = datetime.datetime.now().strftime("%d/%M/%Y/%s")
    date: datetime.date = datetime.datetime.date(datetime.datetime.now())
    tax_rate: float = 0.0

    @property
    def subtotal(self) -> float:
        _sum = None
        for item in self.items:
            if _sum is None:
                _sum = item 
            else:
                _sum += item 
        return _sum
    
    @property
    def tax(self) -> float:
        return self.subtotal * self.tax_rate
    
    @property
    def total(self) -> float:
        return self.subtotal + self.tax