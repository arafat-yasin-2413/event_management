from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
        
        labels = {
            'name' : 'Category Name:',
            'description' : 'Category Description:',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "w-full p-2 rounded-md border-4 focus:outline-none",
                'placeholder': 'Enter category name',
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 rounded-md border-4 focus:outline-none',
                'placeholder':'Write category description',
                'rows':4,
            }),
        }