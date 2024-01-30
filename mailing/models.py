from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='имя')
    surname = models.CharField(max_length=150, verbose_name='фамилия', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email} - {self.name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема')
    body = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    PERIODS = (
        ('daily', 'раз в день'),
        ('weekly', 'раз в неделю'),
        ('monthly', 'раз в месяц'),
    )

    STATUSES = (
        ('created', 'создана'),
        ('started', 'выполняется'),
        ('done', 'завершена'),
    )

    time_start = models.DateTimeField(verbose_name='время старта')
    time_end = models.DateTimeField(verbose_name='время окончания')
    period = models.CharField(default='daily', max_length=15, choices=PERIODS, verbose_name='периодичность')
    status = models.CharField(default='created', max_length=15, choices=STATUSES, verbose_name='статус')

    client = models.ManyToManyField(Client, verbose_name='клиент')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
        return f'С {self.time_start} по {self.time_end}: {self.period}, {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки '


class Logs(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='время последней попытки')
    status = models.CharField(max_length=20, verbose_name='статус попытки')
    response = models.CharField(max_length=250, verbose_name='ответ почтового сервера', **NULLABLE)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.date} - {self.status}'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
