from django.shortcuts import render, redirect
from . forms import CategoryForm
from . models import Category

# Create your views here.

def category_form_creating(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_create')
    else:
        form = CategoryForm()
    return render(request, 'categories/category.html', {'form':form})


def showing_all_category(request):
    all_category = Category.objects.all()
    return render(request,'categories/category.html', {'all_cat':all_category})


def update_category(request, id):
    category = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_show')
    else:
        form = CategoryForm(instance= category)
    return render(request,'categories/category.html', {'form':form})



def delete_category(request, id):
    category = Category.objects.get(pk = id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_show')
    return render(request,'categories/category_delete.html', {'category':category})


