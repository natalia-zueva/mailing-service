from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    MailingDetailView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, MessageListView, \
    MessageCreateView, MessageUpdateView, MessageDeleteView, MessageDetailView, MainView

app_name = MailingConfig.name

urlpatterns =[
    path('', cache_page(60)(MainView.as_view()), name='index'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('mailing/view/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('message/view/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
]