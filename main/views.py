from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'I Putu Gede Kimi Agastya',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)