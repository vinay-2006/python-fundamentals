# fees.py
from typing import List, Dict
from datetime import datetime

class FeesManager:
    """Manages a student's total fees, payments, balance, and history."""
    
    def __init__(self, total: float = 0.0, paid: float = 0.0):
        if total < 0 or paid < 0:
            raise ValueError("Amounts must be non-negative")
        self.total = float(total)
        self.paid = float(paid)
        self.history: List[Dict] = []

    def set_total(self, total: float):
        """Sets the total fees due."""
        if total < 0:
            raise ValueError("Total must be non-negative")
        self.total = float(total)

    def can_pay(self, amount: float) -> bool:
        """Helper to check if a payment is valid (positive and not overpaying)."""
        return amount > 0 and (self.paid + amount <= self.total)

    def pay(self, amount: float):
        """Records a fee payment, raising ValueError on invalid amount or overpayment."""
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        if not self.can_pay(amount):
            raise ValueError(f"Overpayment is not allowed. Max remaining balance is {self.balance():.2f}.")
        
        self.paid += float(amount)
        # Record payment with UTC timestamp
        self.history.append({"amount": float(amount), "ts": datetime.utcnow().isoformat()})

    def balance(self) -> float:
        """Calculates the remaining balance due."""
        return self.total - self.paid

    def as_dict(self) -> Dict:
        """Returns the fees data as a dictionary for serialization."""
        return {"total": self.total, "paid": self.paid, "history": list(self.history)}