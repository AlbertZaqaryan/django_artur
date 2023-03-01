from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import (HomeSlider, HomeSliderActive, 
                     Category, SubCategory, Product,
                     ForZhenya)
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

class HomeListView(ListView):
    template_name = 'main/index.html'

    def get(self, request):

        for_zhenya_name = ForZhenya.objects.all()[0]
        tertox = HomeSliderActive.objects.all()[0]
        tertvox = HomeSlider.objects.all()
        category_list = Category.objects.all().order_by('name')
        product_list = Product.objects.all()
        brand_list = SubCategory.objects.all()
        return render(request, self.template_name, context={
            'tertox':tertox,
            'tertvox':tertvox,
            'category_list':category_list,
            'product_list':product_list,
            'brand_list':brand_list,
            'for_zhenya_name':for_zhenya_name
        })

class ShopListView(ListView):
    template_name = 'main/shop.html'

    def get(self, request, id):
        for_zhenya_name = ForZhenya.objects.all()[0]
        products = SubCategory.objects.filter(pk=id)
        brand_list = SubCategory.objects.all()
        category_list = Category.objects.all().order_by('name')
        

        return render(request, self.template_name, context={
            'products':products, 
            'category_list':category_list,
            'brand_list':brand_list,
            'for_zhenya_name':for_zhenya_name
            })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")