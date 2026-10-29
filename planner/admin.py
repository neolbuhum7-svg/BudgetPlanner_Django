from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "category", "transaction_type", "date")
    list_filter = ("transaction_type", "category", "date")
    search_fields = ("title", "category")
