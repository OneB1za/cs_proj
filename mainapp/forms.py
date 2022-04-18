# from django.forms import forms
from django import forms
from captcha.fields import CaptchaField
from .models import Comments

'''Форма для обратной связи/feedback'''


# не лучшая форма для теста капчи и фидбека
class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, label='Имя')
    email = forms.EmailField(max_length=96, label='Email')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


# форма для комментариев
class CommentsForm(forms.ModelForm):
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
