from django.forms import ModelForm, ModelChoiceField, RadioSelect

from .models import Reviews, Rating, RatingStar


class ReviewForm(ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class RatingForm(ModelForm):
    """Форма добавления рейтинга"""
    star = ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
