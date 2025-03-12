from django.shortcuts import render, redirect
from . forms import CategoryForm


# Create your views here.

def category_form_creating(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_create')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form':form})

