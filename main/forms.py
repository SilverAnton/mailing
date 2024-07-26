from django import forms
from main.models import ServiceClient, ClientMessage, Mailing


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
