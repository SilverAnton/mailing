from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import ClientForm, MessageForm, MailingForm
from main.models import ServiceClient, ClientMessage, Mailing


class BasePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
    #success_url = reverse_lazy("main:index")


class ClientDetailView(DetailView):
    model = ServiceClient
    #success_url = reverse_lazy("main:index")


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
    #success_url = reverse_lazy("main:index")


class MessageDetailView(DetailView):
    model = ClientMessage
    #success_url = reverse_lazy("main:message_list")


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


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("main:mailing_list")