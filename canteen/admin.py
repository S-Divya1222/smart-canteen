from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student_name',
        'register_number',
        'phone_number',
        'total_price',
        'status',
        'order_date',
    )

    list_filter = (
        'status',
        'order_date',
    )

    search_fields = (
        'student_name',
        'register_number',
        'phone_number',
    )

    list_editable = (
        'status',
    )

    ordering = (
        '-order_date',
    )