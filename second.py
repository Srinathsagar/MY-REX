from typing import List
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str

@dataclass(frozen=True)
class Employee:
    name: str
    id: str
    date_of_joining: date
    addresses: List[Address]

# Example Usage
address1 = Address("123 Main St", "CityA", "StateA")
address2 = Address("456 Oak St", "CityB", "StateB")
employee = Employee("John Doe", "E123", date(2020, 5, 1), [address1, address2])
print(employee)
