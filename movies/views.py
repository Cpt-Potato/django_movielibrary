from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from movies.models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            parent = request.POST.get('parent')
            if parent:
                form.parent_id = int(parent)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
