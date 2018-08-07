from django import forms
from complain_app.models import Complain

class ComplainForm(forms.ModelForm):

    class Meta():
        model = Complain
        fields = ('title','text','room',)

        #widgets = {
        #    'title':forms.TextInput(attrs={'class':'textinputclass'}),
        #    'text':forms.Textarea(attrs={'class':'editable medium-editor post-content'})
