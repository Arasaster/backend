from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def biography(request):
    return render(request, 'core/biography.html')

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

    return render(request, 'core/index.html')