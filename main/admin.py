from django.contrib import admin

from main.models import ServiceClient, Mailing, ClientMessage, TryToSend


@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "name",
        "comment",
        "owner",
    )
    search_fields = (
        "email",
        "name",
        "owner"
    )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "start_time",
        "end_time",
        "periodicity",
        "status",
        "client_message",
        "owner",
    )
    search_fields = (
        "start_time",
        "end_time",
        "periodicity",
        "status",
        "client_message",
        "owner",
    )


@admin.register(ClientMessage)
class ClientMessageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "message",
        "owner",
    )
    search_fields = (
        "title",
        "owner",
    )



@admin.register(TryToSend)
class TryToSendAdmin(admin.ModelAdmin):
    list_display = (
        "time",
        "status",
        "server_response",
        "mailing_list",
        "client",
    )
    search_fields = (
        "time",
        "status",
        "server_response",
        "mailing_list",
        "client",
    )
