from django.shortcuts import render,redirect

# Create your views here.
from .forms import BookFrm
from django.contrib import messages
from .models import Book

def book_create(req):
    if req.method=="POST":
        fm = BookFrm(req.POST)
        if fm.is_valid():
            messages.success(req,"Successfully added book")
            fm.save()
        return redirect("/book/new/")
    else:
        form = BookFrm()
        return render(req,"book/book_form.html",{"frm":form})
    
def book_list(req):
    genre = req.GET.get("genre")
    if genre:
        obj = Book.objects.filter(genre=genre)
    else:
        obj = Book.objects.all().order_by("created_at")
    return render(req,"book/book_list.html",{"lst":obj})

def book_detail(req,bk_id):
    book = Book.objects.get(pk=bk_id)
    return render(req,"book/book_details.html",{"bk":book})

def update_detail(req,bk_id):
    form = Book.objects.get(pk=bk_id)
    if req.method=="POST":
        form = BookFrm(req.POST,instance=form)
        if form.is_valid():
            form.save()
            return redirect("book-detail", bk_id=bk_id)
    else:
        form = BookFrm(instance=form)
    
    return render(req,"book/book_form.html",{'frm':form})

def delete_book(req, bk_id):
    book = Book.objects.get(pk=bk_id)
    
    if req.method == "POST":
        book.delete()
    return redirect("book-list")