from django.db import models
from django.core.validators import MinValueValidator

class Transaction(models.Model):
    INCOME = "income"
    EXPENSE = "expense"
    TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    title = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    category = models.CharField(max_length=40)
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"{self.title} - {self.amount}"
