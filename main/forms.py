from django import forms
from django.forms import BooleanField

from main.models import ServiceClient, ClientMessage, Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.fields.items():

            if isinstance(v, BooleanField):
                v.widget.attrs['class'] = 'form-check-input'
            else:
                v.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = ['email', 'name', 'comment', 'owner']


class MessageForm(forms.ModelForm):
    class Meta:
        model = ClientMessage
        fields = ['title', 'message', 'owner']


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['start_time', 'end_time', 'periodicity', 'client_list', 'client_message', 'owner']


class MailingManagerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('status',)
