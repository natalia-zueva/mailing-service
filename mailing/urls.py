from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import index, MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    MailingDetailView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns =[
    path('', index, name='index'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('mailing/view/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]