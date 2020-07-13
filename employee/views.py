from django.shortcuts import render
from employee.models import Customer
# Create your views here.
def index(request):
    cst = Customer.objects.all().order_by('date').order_by('status')
    return render(request,"index.html",{'cst':cst})
