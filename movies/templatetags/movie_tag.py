from django import template

from movies.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/recently_added.html')
def get_recently_added(count=5):
    """Вывод последних добавленных фильмов"""
    movies = Movie.objects.order_by('id')[:count]
    return {'recently_added': movies}
