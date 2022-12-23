from django.shortcuts import render, redirect
from App.models import Category, Product, UserCreateForm
from django.contrib.auth import authenticate, login


def Master(request):
    return render(request, 'master.html')


def Index(request):
    category = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        product = Product.objects.filter(sub_category=category_id).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'index.html', context)


def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],

            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreateForm()
    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)
