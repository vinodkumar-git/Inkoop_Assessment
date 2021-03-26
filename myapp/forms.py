from django import forms

class DocumentForm(forms.Form):
    height = forms.IntegerField(label='Set Image Height',)
    width = forms.IntegerField(label='set Image width',)
    docfile = forms.FileField(
        label='Select a file',
    )
    fnal_docfile = forms.FileField(
        label='Select another file',
    )
