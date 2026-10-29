from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["title", "amount", "category", "transaction_type"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Monthly allowance",
                "class": "field",
            }),
            "amount": forms.NumberInput(attrs={
                "placeholder": "0.00",
                "min": "0.01",
                "step": "0.01",
                "class": "field",
            }),
            "category": forms.Select(attrs={"class": "field"}, choices=[
                ("Food", "Food"),
                ("Travel", "Travel"),
                ("Shopping", "Shopping"),
                ("Education", "Education"),
                ("Salary", "Salary"),
                ("Bills", "Bills"),
                ("Other", "Other"),
            ]),
            "transaction_type": forms.Select(attrs={"class": "field"}),
        }
        labels = {
            "title": "Transaction title",
            "amount": "Amount (₹)",
            "category": "Category",
            "transaction_type": "Type",
        }
