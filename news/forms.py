from django import forms


class EntryForm(forms.Form):
    """ Тестовый класс сбора ресурсов
    """
    height = forms.IntegerField()
    height_random = forms.HiddenInput()
