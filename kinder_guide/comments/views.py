from django.shortcuts import redirect
from django.views.generic import DetailView

from ..education.models import Education
from .models import Review
from .forms import ReviewForm


class PageDetailView(DetailView):
    template_name = 'sample_page.html'
    model = Education

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        connected_reviews = Review.objects.filter(
            ReviewPost=self.get_object()
        )
        number_of_reviews = connected_reviews.count()
        data['reviews'] = connected_reviews
        data['number_of_review'] = number_of_reviews
        data['review_form'] = ReviewForm()
        return data

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                content = review_form.cleaned_data['content']
                try:
                    parent = review_form.cleaned_data['parent']
                except KeyError:
                    parent = None

            new_review = Review(
                content=content,
                author=request.user,
                ReviewPost=self.get_object(),
                parent=parent,
            )
            new_review.save()
            return redirect(request.path_info)
