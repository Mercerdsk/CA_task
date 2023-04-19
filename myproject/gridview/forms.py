from django import forms
from .models import Notify

class NotifyForm(forms.ModelForm):
    class Meta:
        model = Notify
        fields = ('notification_title', 'notification_text','notification_image','notication_name')
