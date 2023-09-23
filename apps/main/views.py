from django.shortcuts import render, redirect
from django.views.generic import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from .models import Product, Order, User


class MainView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'index.html'
        products: QuerySet[Product] = Product.objects.all()
        return render(
            request=request,
            template_name=template_name,
            context={
                'products': products
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'index.html'
        data = request.POST.getlist('ch')
        for i in data:
            Order.objects.create(
                user=User.objects.first(),
                product=Product.objects.filter(name=i)[0]
            )
        return redirect('/')
    

class CreateView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'index2.html'
        return render(
            request=request,
            template_name=template_name,
            context={
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'index2.html'
        data = request.POST
        print(data)
        print(data.get('price'))
        Product.objects.create(
            name=data.get('name'),
            price=data.get('price')
        )
        return redirect('/')