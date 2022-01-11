from django.urls import path
from . import views

app_name = "finance"
urlpatterns = [path('cust', views.customers, name="cust"),
               path('', views.home, name='home'),
               path('<int:cust_id>', views.transfer, name='transfer')]
