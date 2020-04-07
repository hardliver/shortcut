from django import forms

class ShortcutForm(forms.Form):
    web_addr = forms.URLField(label='Web Address', max_length=300)