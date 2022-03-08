from django.shortcuts import render

def main_page(request):
    if request:
        return render(request, 'index.html')
