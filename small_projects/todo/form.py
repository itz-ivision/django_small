from django import forms


class TodoForm(forms.Form):
    attributes = {
        'class':  'form-control',
        'placeholder': 'Enter todo e.g. Delete junk files',
        'aria-label': 'Todo',
        'aria-describedby': 'add-btn',
    }
    text = forms.CharField(max_length=40, widget=forms.TextInput(attrs=attributes))
