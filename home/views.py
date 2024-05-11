from django.shortcuts import render

def handler404(request, exception):
    return render("exceptions/ex404.html", status=404)