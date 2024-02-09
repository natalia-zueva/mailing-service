import random

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from blog.models import Article
from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import Mailing, Client, Message


# def index(request):
#     context = {
#         'title': 'Сервис рассылок'
#     }
#     if request.method == 'GET':
#         return render(request, 'mailing/index.html', context)

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Сервис рассылок'

        context_data['mailing'] = len(Mailing.objects.all())
        context_data['started_mailing'] = Mailing.objects.filter(status=Mailing.STARTED).count()
        context_data['client'] = len(Client.objects.all())
        context_data['object_list'] = random.sample(list(Article.objects.all()), 3)

        return context_data


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    permission_required = 'mailing.view_mailing'
    extra_context = {
        'title': 'Рассылки'
    }


class MailingCreateView(PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.add_mailing'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:update_mailing', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.client != self.request.user:
            raise Http404
        return self.object


class MailingDeleteView(PermissionRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
    permission_required = 'mailing.delete_mailing'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    permission_required = 'mailing.view_client'
    extra_context = {
        'title': 'Клиенты'
    }


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailing:update_client', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения для рассылок'
    }


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'mailing.change_message'

    def get_success_url(self):
        return reverse('mailing:update_message', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message_detail.html'
