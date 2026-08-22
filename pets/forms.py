from django import forms
from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'sex', 'size', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full h-12 border border-gray-400 rounded px-4',
            }),
            'age': forms.TextInput(attrs={
                'class': 'w-full h-12 border border-gray-400 rounded px-4',
                'type': 'number',
            }),
            'sex': forms.Select(attrs={
                'class': 'w-full h-12 border border-gray-400 rounded px-4',
            }),
            'size': forms.Select(attrs={
                'class': 'w-full h-12 border border-gray-400 rounded px-4',
            }),
            'icon': forms.FileInput(),
        }
        error_messages = {
            'name': {
                'required': 'ペットの名前を入力してください。',
            },
            'age': {
                'required': '年齢を入力してください。',
            },
            'sex': {
                'required': '性別を選択してください。',
            },
            'size': {
                'required': 'サイズを選択してください。',
            },
        }
