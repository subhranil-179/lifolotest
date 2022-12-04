from django import forms

class CommentForm(forms.Form):
    message = forms.CharField(label='',
                              max_length=200,
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control',
                                         'placeholder':"Type comment..."
                                         }
                                  )
                              )
