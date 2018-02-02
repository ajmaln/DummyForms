from django import forms


class IndexForm(forms.Form):

    def __init__(self, data):
        super(IndexForm, self).__init__()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

    CHOICES = ((1, 'MALE'), (2, "FEMALE"))
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=CHOICES)
    about_me = forms.CharField(widget=forms.Textarea)
