from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs")
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {"form": form})
