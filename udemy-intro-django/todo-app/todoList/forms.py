from django import forms

class todoListForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class':'form-control w-100', 'placeholder':'New Task', 'aria-label':'Todo', 'aria-describeby':'add button'}
        )
    )

