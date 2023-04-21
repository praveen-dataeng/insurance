from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='pres-home'),
    path('pp/', Home.as_view(template_name='presparser/prescription.html'), name='pres-prescription'),
    path('pd/', Home.as_view(template_name='presparser/patientdetails.html'), name='pres-patient'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)