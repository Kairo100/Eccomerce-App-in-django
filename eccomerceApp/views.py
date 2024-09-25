from django.shortcuts import get_object_or_404, render

from .models import Product

# Create your views here.
def Products(request):
    pro = Product.objects.all()

    context={
        'pro':pro
    }
    return render (request,'index.html',context)

def Products_details(request, p_id):
    prod = get_object_or_404(Product, id=p_id)
    return render(request, 'Product_details.html',{'prod':prod})