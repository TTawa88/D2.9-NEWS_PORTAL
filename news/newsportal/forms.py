from django.forms import ModelForm, BooleanField
from .models import Post



class PostForm(ModelForm):
    check_box = BooleanField(label='Галочка!')

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'categoryType', 'check_box']