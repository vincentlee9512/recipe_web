from django import forms
from .models import Blog, Comment


class NewBlogForm(forms.ModelForm):
    CATEGORY_CHOICE = (
        '家常菜',
        '便当',
    )

    class Meta:
        model = Blog
        exclude = ('author', )
        fields = ('title', 'description', 'cover', 'category',
                  'ingredient', 'step_1', 'step_1_photo',
                  'step_2', 'step_2_photo', 'step_3', 'step_3_photo',
                  'step_4', 'step_4_photo', 'step_5', 'step_5_photo',
                  'step_6', 'step_6_photo', 'step_7', 'step_7_photo',
                  'step_8', 'step_8_photo', 'step_9', 'step_9_photo',
                  'step_10', 'step_10_photo')

        CATEGORY_CHOICE = (
            ('家常菜', '家常菜'),
            ('便当', '便当'),
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={'class': 'form-control'}),

            'category': forms.Select(choices=CATEGORY_CHOICE, attrs={'class': 'form-control'}),

            'ingredient': forms.Textarea(attrs={'class': 'form-control'}),

            'step_1': forms.Textarea(attrs={'class': 'form-control'}),

            'step_2': forms.Textarea(attrs={'class': 'form-control'}),

            'step_3': forms.Textarea(attrs={'class': 'form-control'}),

            'step_4': forms.Textarea(attrs={'class': 'form-control'}),

            'step_5': forms.Textarea(attrs={'class': 'form-control'}),

            'step_6': forms.Textarea(attrs={'class': 'form-control'}),

            'step_7': forms.Textarea(attrs={'class': 'form-control'}),

            'step_8': forms.Textarea(attrs={'class': 'form-control'}),

            'step_9': forms.Textarea(attrs={'class': 'form-control'}),

            'step_10': forms.Textarea(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'recipe')
        fields = ('comment', )

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
