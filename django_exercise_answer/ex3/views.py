from django.shortcuts import render

def input1(request):
    return render(request, 'input1.html')

def show1(request):
    inp = request.POST['inp']
    ctx = {
        'inp': inp,
    }
    return render(request, 'show1.html', ctx)

def input2(request, param1):
    ctx = {
        'inp': param1,
    }
    return render(request, 'show1.html', ctx)

