from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Pizza, Topping, Comment
from .forms import PizzaForm, ToppingForm, CommentForm

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
    comments = pizza.comment_set.order_by('-date_added')
    toppings = pizza.topping_set.order_by('name')
    pizza_type = lookup(pizza_id)

    context = {'pizza': pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'MainApp/pizza.html', context)


def lookup(pizza_id):
    if pizza_id == 1:
        p_type = "1"
    elif pizza_id == 2:
        p_type = "2"
    elif pizza_id == 3:
        p_type = "3"
    elif pizza_id == 4:
        p_type = "4"
    else:
        p_type = "5"

    #keys = {'1':'Pepperoni', '2':'Cheese', '3':'Hawaiian', '4':'MeatLovers', '5':'Supreme'}
    return p_type

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

@login_required
#new_entry
def new_comm(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comm = form.save(commit=False)
            #passing the actual object
            new_comm.username = request.user
            new_comm.pizza = pizza
            new_comm.save()
            return redirect('MainApp:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'MainApp/new_comm.html', context)
