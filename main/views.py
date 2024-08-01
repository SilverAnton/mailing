from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from mailing_blog.services import get_blog_list_from_cache
from main.forms import ClientForm, MessageForm, MailingForm, MailingManagerForm
from main.models import ServiceClient, ClientMessage, Mailing
from main.services import get_client_list_from_cache, get_message_list_from_cache


class BasePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings = Mailing.objects.all()
        clients = ServiceClient.objects.all()
        messages = ClientMessage.objects.all()
        context_data['all_mailings'] = mailings.count()
        context_data['active_mailings'] = mailings.filter(status=Mailing.STARTED).count()
        context_data['active_clients'] = clients.values('email').distinct().count()
        context_data['all_messages'] = messages.count()
        context_data['random_blogs'] = get_blog_list_from_cache().order_by('?')[:3]
        return context_data



################################################################

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = ServiceClient
    form_class = ClientForm
    success_url = reverse_lazy("main:client_list")

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientListView(ListView):
    model = ServiceClient

    #def get_queryset(self, queryset=None):
        #queryset = super().get_queryset()
        #user = self.request.user
        #if not user.is_superuser:
            #queryset = get_client_list_from_cache().filter(owner=self.request.user)
        #return queryset

    #def get_queryset(self):
        #return get_client_list_from_cache()


class ClientDetailView(DetailView):
    model = ServiceClient


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceClient
    form_class = ClientForm
    success_url = reverse_lazy("main:client_update")

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = ServiceClient
    success_url = reverse_lazy("main:client_list")


################################################################


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = ClientMessage
    form_class = MessageForm
    success_url = reverse_lazy("main:message_list")

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = ClientMessage

    def get_queryset(self):
        return get_message_list_from_cache()


class MessageDetailView(DetailView):
    model = ClientMessage


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientMessage
    form_class = MessageForm
    success_url = reverse_lazy("main:message_list")

    def form_valid(self, form):
        message_ = form.save()
        user = self.request.user
        message_.owner = user
        message_.save()
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = ClientMessage
    success_url = reverse_lazy("main:message_list")


################################################################


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("main:mailing_list")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)




class MailingDetailView(DetailView):
    model = Mailing


class MailingListView(ListView):
    model = Mailing


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    #form_class = MailingForm
    success_url = reverse_lazy("main:mailing_list")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingForm
        elif user.has_perm("main.can_edit_status"):
            return MailingManagerForm
        raise PermissionDenied




class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("main:mailing_list")
