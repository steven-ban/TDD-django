from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.exceptions import ValidationError

from models import Item, List
from forms import ItemForm

# Create your views here.

# def view_list(request, list_id) : 
#     list_ = List.objects.get(id = list_id)
#     if request.method == 'POST' : 
#         Item.objects.create(text = request.POST['item_text'], list = list_)
#         return redirect('/lists/%d/' % (list_.id))
#     return render(request, 'list.html', {'list' : list_})
    

# def new_list(request) : 
#     list_ = List.objects.create()
#     item = Item.objects.create(text = request.POST['item_text'], list = list_)
#     try : 
#         item.full_clean()
#         item.save()
#     except ValidationError : 
#         list_.delete()
#         error = "You cannot have an empty list item."
#         return render(request, 'home.html', {"error" : error})
#     return redirect('lists/%d/' % (list_.id,))
    
# def add_item(request) : 
#     # list_ = List.objects.get(id = list_id)
#     # Item.objects.create(text = request.POST['item_text'], list = list_)
#     # return redirect('lists/%d/' % (list_.id, ))
#     form = ItemForm(request.POST)
#     if form.is_valid() : 
#         form.save()
       
#         return render(request, 'add.html', {'form' : form})
#     else : 
#         return redirect('/')

def home_page(request):
    listInput = request.POST['list_text']
    listInc = List.objects.filter(text = listInput)
    if not listInc :
        list2 = List.objects.create(text = listInput)
        list2.save()
    listInc2 = List.objects.get(text = listInput)
    item = Item.objects.create(text = request.POST['item_text'], the_list = listInc2)

    item.save()
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})  
    

