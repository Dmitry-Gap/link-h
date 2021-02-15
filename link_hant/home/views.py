from django.shortcuts import render
from home.forms import QuickContactForms


def home_page(request):
    context = {}
    return render(request, "home.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def contact_page(request):
    if request.method == "POST":
        pass
    context = {
        "form": QuickContactForms()
    }
    return render(request,"contact.html", context)
    