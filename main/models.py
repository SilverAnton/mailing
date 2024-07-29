from django.db import models

from users.models import User


class ServiceClient(models.Model):
    email = models.EmailField(unique=True, verbose_name="email")
    name = models.CharField(max_length=100, verbose_name="name")
    comment = models.TextField(verbose_name="comment")
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "сервисный клиент"
        verbose_name_plural = "сервисные клиенты"


class ClientMessage(models.Model):
    title = models.CharField(max_length=150, verbose_name="тема сообщения")
    message = models.TextField(verbose_name='текст сообщения')
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение клиенту'
        verbose_name_plural = 'сообщения клиентам'


class Mailing(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]
    start_time = models.DateTimeField(verbose_name='дата и время начала рассылки')
    end_time = models.DateTimeField(verbose_name='дата и время окончания рассылки')
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name='статус')
    client_list = models.ManyToManyField(ServiceClient, verbose_name='клиент')
    client_message = models.ForeignKey(ClientMessage, verbose_name='Сообщение', on_delete=models.CASCADE, null=True,
                                       blank=True)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return f'time: {self.start_time} - {self.end_time}, periodicity: {self.periodicity}, status: {self.status}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылок'
        permissions = [
            ("can_edit_status", "can edit status"),
        ]


class TryToSend(models.Model):
    DONE = 'Попытка успешна'
    FALL = 'Попытка не успешна'
    STATUS_CHOICES = [
        (DONE, "Успешно"),
        (FALL, "Не успешно"),
    ]

    time = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='статус попытки')
    server_response = models.CharField(verbose_name='ответ почтового сервера', null=True, blank=True)

    mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey(ServiceClient, on_delete=models.CASCADE, verbose_name='клиент')

    def __str__(self):
        return f'{self.time} {self.status}'

    class Meta:
        verbose_name = 'попытка отправления'
        verbose_name_plural = 'попытки отпраления'

#не забудь сделать миграции всех моделей и применить их!
