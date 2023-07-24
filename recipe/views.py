from django.shortcuts import render , redirect
from .models import Rescipe
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    AllRecipes = Rescipe.objects.all()
    user = False
    if  request.user.is_authenticated:
        user = True
        params = {"Recipes":AllRecipes, "user":user}

        return render(request, "home.html", params)
    else:
        params = {"Recipes":AllRecipes, "user":user}
        return render(request , "home.html" , params)


def searchMatch(query, item):
    if query in item.title or query in item.desc:
        return True
    else:
        return False

def serach(request):
        query = request.GET.get('search')
        allProds = []
        catprods = Rescipe.objects.values('desc','id')
        cats = {item['desc'] for item in catprods}
        for cat in cats:
            prodtemp = Rescipe.objects.filter(desc=cat)
            prod = [item for item in prodtemp if searchMatch(query,item)]
            if prod:
                params = {"Recipes":prod}
        return render(request, "home.html" , params)
   
        
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if   user has entered correct 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/add/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')   


def logoutUser(request):
    logout(request)
    return redirect("/")

def singupUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "you have been successfully singup")
        print(f"user is create username: {username}")
        return redirect("/login")
    else:
        return redirect("/user")

    



def AddRecipe(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        source = request.POST.get("source")
        print(title, desc, source)
        recipe = Rescipe(title=title, desc = desc, url = source )
        recipe.save()
    return render(request, "add.html")
