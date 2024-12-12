from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Nhập tin nhắn của bạn...', 'class': 'p-4 text-black', 'maxlength': '300', 'autofocus': True}),
            
        }

class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'placeholder': 'Nhập tên nhóm của bạn...', 
                'class': 'p-4 text-black', 
                'maxlength': '300', 
                'autofocus': True
                }),
        }
        
class ChatRoomEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'class': 'p-4 text-black font-bold mb-4', 
                'maxlength': '300', 
                }),
        }