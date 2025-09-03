from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406351024',
        'name': 'Raihan Maulana Heriandry',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)