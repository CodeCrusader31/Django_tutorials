from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import userProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# class createProfileView(CreateView):    
#     template_name = "profiles/create_profile.html"
#     model = userProfile
#     fields = "__all__"
#     success_url = "/profiles"

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # user_image = submitted_form.cleaned_data["user_image"]
            # store_file(user_image)
            profile = userProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html",{
            "form": submitted_form
        })
    

class ProfilesView(ListView):
    model = userProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"
