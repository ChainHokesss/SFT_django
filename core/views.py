from rest_framework.views import APIView
from rest_framework import response

from core.models import LoanApplication


class LoanApplicationView(APIView):
    def get(self, request, contract_id):
        values = LoanApplication.objects.filter(
            contract=contract_id,
            products__isnull=False,
        ).values_list('products__manufacturer_id', flat=True).distinct()

        if not values:
            return response.Response(status=404)

        return response.Response(values)
