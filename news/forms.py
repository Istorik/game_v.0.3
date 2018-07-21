from django import forms


class EntryForm(forms.Form):
    """ Тестовый класс сбора ресурсов
    """
    name = forms.CharField(max_length=100)
    height = forms.IntegerField()
    height_random = forms.HiddenInput()
