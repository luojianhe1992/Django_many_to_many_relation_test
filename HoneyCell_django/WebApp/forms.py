from django import forms

from WebApp.models import *

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ['headline', 'content', 'publications']

        widgets = {'headline': forms.TextInput,
                   'content': forms.Textarea}

    def clean(self):

        print("in the function of clean in ArticleModelForm.")

        cleaned_data = super(ArticleModelForm, self).clean()

        headline = self.cleaned_data.get('headline')
        content = self.cleaned_data.get('content')
        publications = self.cleaned_data.get('publications')

        print("%" * 30)
        print(cleaned_data)
        print("%" * 30)

        return cleaned_data

    def clean_headline(self):

        print("in the function of clean_headline in ArticleModelForm.")

        headline = self.cleaned_data.get('headline')

        if not headline:
            print("Please type in article headline.")
            raise forms.ValidationError("Please type in article headline.")

        return headline

    def clean_content(self):

        print("in the function of clean_content in ArticleModelForm.")

        content = self.cleaned_data.get('content')

        if not content:
            print("Please type in article content.")
            raise forms.ValidationError("Please type in article content.")

        return content