from django import forms

from mailing.models import Mailing, Client, Message


class StyleFormMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ('status', 'client')


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email', 'name', 'surname',)


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = ('title', 'body',)