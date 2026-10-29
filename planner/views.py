from decimal import Decimal
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TransactionForm
from .models import Transaction

def dashboard(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction added successfully.")
            return redirect("dashboard")
        messages.error(request, "Please check the form and correct any errors.")
    else:
        form = TransactionForm()

    income = (
        Transaction.objects.filter(transaction_type=Transaction.INCOME)
        .aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    )
    expenses = (
        Transaction.objects.filter(transaction_type=Transaction.EXPENSE)
        .aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    )

    context = {
        "form": form,
        "transactions": Transaction.objects.all(),
        "income": income,
        "expenses": expenses,
        "balance": income - expenses,
    }
    return render(request, "planner/dashboard.html", context)

def delete_transaction(request, pk):
    if request.method == "POST":
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        messages.success(request, "Transaction deleted.")
    return redirect("dashboard")
