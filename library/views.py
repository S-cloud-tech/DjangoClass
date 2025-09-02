from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    template_name = "index.html"
    return render(request, template_name=template_name)

def show_categories(request):
    category = Category.objects.all()

    return render(request, "category.html", {"category": category})

def show_book(request):
    books = Book.objects.all()

    return render(request, "books.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "books.html", {"books": Book.objects.all()})
        else:
            return render(request, "add_book.html", {"form": form})
    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("library:show_book")
        else:
            return render(request, "add_book.html", {"form": form})
    else:
        return render(request, "add_book.html", {"form": form})

        
