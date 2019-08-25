from django import forms
from .models import Blog


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
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'category': forms.Select(choices=CATEGORY_CHOICE, attrs={'class': 'form-control'}),

            'ingredient': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_1': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_2': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_3': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_4': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_5': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_6': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_7': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_8': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_9': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'step_10': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


# # 作者
#     author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#
#     # 菜名、封面、简介、分类、成分
#     title = models.CharField(max_length=100)
#     cover = models.ImageField(upload_to='photos/%Y/%m/%d')
#     description = models.TextField(blank=True)
#     category = models.CharField(max_length=100)
#     ingredient = models.TextField()
#
#     # 上传时间
#     post_date = models.DateTimeField(default=datetime.now, blank=True)
#
#     # 步骤，只有步骤1的文字描述是必须的
#     step_1 = models.TextField()
#     step_1_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_2 = models.TextField(blank=True)
#     step_2_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_3 = models.TextField(blank=True)
#     step_3_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_4 = models.TextField(blank=True)
#     step_4_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_5 = models.TextField(blank=True)
#     step_5_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_6 = models.TextField(blank=True)
#     step_6_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_7 = models.TextField(blank=True)
#     step_7_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_8 = models.TextField(blank=True)
#     step_8_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_9 = models.TextField(blank=True)
#     step_9_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
#     step_10 = models.TextField(blank=True)
#     step_10_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)