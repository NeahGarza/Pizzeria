from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Pizza, Topping
#from .forms import PizzaForm, ToppingForm

# Create your views here.

def index(request):
    '''Home page for Neah's Python Pizzeria!'''
    return render(request, 'MainApp/index.html')


def pizzas(request):
    #CHECK NEXT LINE
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, 'MainApp/pizzas.html', context)
    

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    print(pizza_id)
    pizza.pizza_type = lookup(pizza_id)

    context = {'pizza': pizza, 'toppings':toppings}

    return render(request, 'MainApp/pizza.html', context)


def lookup(pizza_id):
    #keys = {'Cheese':'0', 'Hawaiian':'1', 'MeatLovers':'2', 'Pepperoni':'3', 'Supreme':'4'}
    keys = {'1':'Pepperoni', '2':'Cheese', '3':'Hawaiian', '4':'MeatLovers', '5':'Supreme'}
    value = keys[pizza_id]
    return value



def comments(request, pizza_id):
    if request.method == "GET" and request.GET.get("btn1"):
        comment = request.GET.get("comment")
        Comment.objects.create(post_id=pizza_id, username=request.user, text=comment, date_added=date.today())

    comments = Comment.object.filter(post=pizza_id)
    post = Post.objects.get(id=pizza_id)

    context = {'posts':post, 'comments':comments}
    return render(request, 'MainApp/comments.html', context)

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    if not profile.exists():
        Profile.objects.create(user=request.user)

    profile = Profile.objects.get(user=request.user)   

    if request.method != "POST":
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:profile')

    context = { 'form':form}
    return render(request, 'MainApp/profile.html', context)
