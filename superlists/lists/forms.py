from django.forms import ModelForm

from models import List, Item

class ItemForm(ModelForm) : 
    class Meta:
        model = Item
        fields = ['text', 'the_list']

