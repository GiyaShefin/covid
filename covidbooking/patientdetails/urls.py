from django.urls import path
from . import views

app_name = "patientdetails"


urlpatterns = [
    path("detail",views.detail_patient, name="detail_patient"),
    path('success',views.success_page,name="success_page"),
]