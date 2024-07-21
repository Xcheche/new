from django.shortcuts import render, redirect
from django.http import HttpResponse

from food.forms import ItemForm
from food.models import Item
# Create your views here.
def index(request):
    item_list = Item.objects.all()

    context = {
        "item_list": item_list
    }
    return render(request, "food/index.html", context)


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)  # Fetch single item
    context = {
        "item": item
    }
    return render(request, "food/detail.html", context)
 

def create_item(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm()

    return render(request, "food/item-form.html", {'form': form})



def update_item(request, item_id):

    item = Item.objects.get(pk=item_id)

    if request.method == "POST":
        form = ItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm(instance=item)

    return render(request, "food/item-form.html", {'form': form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    
    return render(request, "food/confirm-delete.html", {'item': item})