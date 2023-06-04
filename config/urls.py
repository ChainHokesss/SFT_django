from django.contrib import admin
from django.urls import include, path

from core.views import LoanApplicationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('<int:contract_id>/', LoanApplicationView.as_view())
]
