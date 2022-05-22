from django.forms import ModelForm

from .models import Reviews


class ReviewForm(ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
