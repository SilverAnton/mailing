from django.urls import path
from django.views.decorators.cache import cache_page
from main.apps import MainConfig
from main.views import HomePageView, ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, \
    ClientDeleteView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView

app_name = MainConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("client_create/main", ClientCreateView.as_view(), name="client_create"),
    path("client_list/main", ClientListView.as_view(), name="client_list"),
    path("client_detail/main/<int:pk>/", cache_page(60)(ClientDetailView.as_view()), name="client_detail"),
    path("client_update/main/<int:pk>/", ClientUpdateView.as_view(), name="client_update"),
    path("client_delete/main/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
    path("message_create/main", MessageCreateView.as_view(), name="message_create"),
    path("message_list/main", MessageListView.as_view(), name="message_list"),
    path("message_detail/main/<int:pk>/", cache_page(60)(MessageDetailView.as_view()), name="message_detail"),
    path("message_update/main/<int:pk>/", MessageUpdateView.as_view(), name="message_update"),
    path("message_delete/main/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),
    path("mailing_create/main", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing_list/main", cache_page(60)(MailingListView.as_view()), name="mailing_list"),
    path("mailing_detail/main/<int:pk>/", cache_page(60)(MailingDetailView.as_view()), name="mailing_detail"),
    path("mailing_update/main/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing_delete/main/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"),

    ]
