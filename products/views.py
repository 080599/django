from django.shortcuts import render, redirect

from products.models import ProductModel, CategoryModel, CartModel
from products.handler import bot

def home_page(request):
    products = ProductModel.objects.all()
    catigories = CategoryModel.objects.all()
    context = {'products': products, 'catigories': catigories}
    return render(request, 'index.html', context=context)


def not_found_page(request):
    return render(request, 'notfound.html')


def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(product_name__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('notfound')


def product_page(request, id):
    product = ProductModel.objects.get(id=id)
    context = {'product': product}
    return render(request, 'single-product.html', context=context)


def about_page(request):
    return render(request, 'about.html')


# Create your views here.
def add_product_to_cart(request, id):
    if request.method == 'POST':
        checker = ProductModel.objects.get(id=id)
        if checker.count >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id, user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count')))
            print('SUCCESS')
            return redirect('/user_cart')
        else:
            print('ERROR')
            return redirect('/')


def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'New order'

        for i in cart:
            main_text += f'\n Product:{i.user_product}\n' \
                         f'\n Count:{i.user_product_quantity}\n' \
                         f'\n ID_user: {i.user_id}\n' \
                         f'\n Price: {i.user_product.price}\n'
            bot.send_message(-1002182319008, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, 'cart.html', context={'cart': cart})
