from django.urls import path
from . import views
app_name = "finance"
urlpatterns = [ path('<str:name>', views.customers, name="cust") ,
path('', views.home, name='home')]