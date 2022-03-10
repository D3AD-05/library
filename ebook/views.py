from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookAddForm, SearchForm
from .models import Books


def home(request):
    context = {
        'posts': Books.objects.all()
    }
    return render(request, 'home.html', context)


@login_required
def addbook(request):
    if request.method == "GET":
        form = BookAddForm()
        return render(request, "addbook.html", {'form': form})
    elif request.method == "POST":  # post-submit |get
        form = BookAddForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            username = form.cleaned_data.get('username')
            messages.success(request, f'book not added')
            return redirect('addbook')
    else:
        form = BookAddForm()
        return render(request, "addbook.html", {"form": form})


def get_books(request):
    if request.user.is_authenticated:
        form = SearchForm()
        context = {}
        boks = Books.objects.all()
        context["boks"] = boks
        context["form"] = form
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                boks = Books.objects.filter(title__contains=title)
                context["boks"] = boks
                return render(request, "list.html", context)
        return render(request, "list.html", context)
    else:
        return redirect("home")


def book_details(request, id):
        book = Books.objects.get(id=id)
        context = {}
        context["book"] = book
        return render(request, "book_detail.html", context)

@login_required()
def remove_book(request,id):
    if request.user.is_authenticated:
      book=Books.objects.get(id=id)
      book.delete()
      return redirect('search')

@login_required
def update_book(request,id):
    if request.user.is_authenticated:
      book=Books.objects.get(id=id)
      form=BookAddForm(instance=book)
      context={}
      context["form"]=form
      if request.method=="POST":
            book=Books.objects.get(id=id)
            form=BookAddForm(instance=book,data=request.POST)
            if form.is_valid():
                form.save()
                # book.title=form.cleaned_data["title"]
                # book.author = form.cleaned_data["author"]
                # book.category = form.cleaned_data["category"]
                # book.price = form.cleaned_data["price"]
                # book.no_copies = form.cleaned_data["no_copies"]
                # book.save()
                return redirect("search")
            else:
                form=BookAddForm(request.POST)
                context["form"]=form

                return render(request, "book_edit.html", context)

      return render(request, "book_edit.html", context)
    else:

        return redirect("details")
