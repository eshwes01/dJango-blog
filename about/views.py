from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    context = {"about": about,"collaborate_form":collaborate_form}
    
    # collab_message = post.comments.all().order_by("-created_on")
    if request.method == "POST":collaborate_form = CollaborateForm(data=request.POST)
    if collaborate_form.is_valid():
            collab= collaborate_form.save(commit=False)
            collab.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request Message has been received !'
            )   

    return render(
        request,
        "about/about.html",
        { 
              "about": about,
              "collaborate_form":collaborate_form
        }

    
    )