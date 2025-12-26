# from django.http import HttpResponseRedirect
# from django.shortcuts import render

# from .forms import ReviewForm

# # Create your views here.

# def review(request):
#   if request.method == 'POST':
#     form = ReviewForm(request.POST)

#     if form.is_valid():
#       print(form.cleaned_data)
#       return HttpResponseRedirect("/thank-you")

#   form = ReviewForm()

#   return render(request, "reviews/review.html", {
#     "form": form
#   })


# def thank_you(request):
#   return render(request, "reviews/thank_you.html")


from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def postT(self, request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        
        request.session["favorite_review"] =  fav_review
        return HttpResponseRedirect("/reviews/" + review_id)

