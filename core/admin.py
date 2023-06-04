from django.contrib import admin

from core.models import (
    Contract,
    LoanApplication,
    Manufacturer,
    Product,
)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
