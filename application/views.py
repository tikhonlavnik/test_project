from django.shortcuts import render


def greeting_page(request):
    if request.method == 'GET':
        data = {
            'name': request.GET.get('name'),
            'message': request.GET.get('message')
        }
    return render(request, 'greeting_page.html', {'data': data})
