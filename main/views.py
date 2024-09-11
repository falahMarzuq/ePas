from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Baju',
        'price': 'Rp1.000.000',
        'description': 'description: Baju dengan kualitas terbaik di Indonesia'
    }

    return render(request, "main.html", context)