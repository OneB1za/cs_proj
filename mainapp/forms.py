
from django import forms
from captcha.fields import CaptchaField
from .models import Comments


class ContactForm(forms.Form):
    """Форма для обратной связи(сырая)..
        учился работать с самой простой капчей"""
    name = forms.CharField(max_length=64, label='Имя')
    email = forms.EmailField(max_length=96, label='Email')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class CommentsForm(forms.ModelForm):
    """Форма для добавления комментариев"""
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text')

# class RatingForm(forms.ModelForm):

# star = forms.ModelChoiceField(
# queryset=RatingStart.objects.all(), widget=forms.RadioSelect(), empty_label=None
# )

# class Meta:
# model = Rating
# fields = ('star',)
