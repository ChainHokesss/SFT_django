from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Contract(BaseModel):
    pass


class Manufacturer(BaseModel):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.id} {self.name}'


class LoanApplication(BaseModel):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        related_name='loan_applications'
    )


class Product(BaseModel):
    name = models.CharField(max_length=60)
    loan_application = models.ForeignKey(
        LoanApplication,
        on_delete=models.PROTECT,
        related_name='products'
    )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} {self.name}'
