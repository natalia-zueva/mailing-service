from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import MailingForm, ClientForm
from mailing.models import Mailing, Client


def index(request):
    context = {
        'title': 'Сервис рассылок'
    }
    if request.method == 'GET':
        return render(request, 'mailing/index.html', context)


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Рассылки'
    }


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailing:update_mailing', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


class ClientListView(ListView):
    model = Client
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




