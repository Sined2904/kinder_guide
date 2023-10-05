from django.shortcuts import redirect
from django.views.generic import DetailView

from ..education.models import Education
from .models import Comment
from .forms import CommentForm


class PageDetailView(DetailView):
    template_name = 'sample_page.html'
    model = Education

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = Comment.objects.filter(
            CommentPost=self.get_object()
        )
        number_of_comments = connected_comments.count()
        data['comments'] = connected_comments
        data['number_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()
        return data

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']
                try:
                    parent = comment_form.cleaned_data['parent']
                except KeyError:
                    parent = None

            new_comment = Comment(
                content=content,
                author=request.user,
                CommentPost=self.get_object(),
                parent=parent,
            )
            new_comment.save()
            return redirect(request.path_info)
