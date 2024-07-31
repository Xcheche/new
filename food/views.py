from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from food.forms import ItemForm
from food.models import Item



# Create your views here.
@login_required
def index(request):
    item_list = Item.objects.all()

    context = {"item_list": item_list}
    return render(request, "food/index.html", context)

@login_required
def detail(request, item_id):
    item = Item.objects.get(pk=item_id)  # Fetch single item
    context = {"item": item}
    return render(request, "food/detail.html", context)

@login_required
def create_item(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm()

    return render(request, "food/item-form.html", {"form": form})

@login_required
def update_item(request, item_id):

    item = Item.objects.get(pk=item_id)

    if request.method == "POST":
        form = ItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm(instance=item)

    return render(request, "food/item-form.html", {"form": form, "item": item})

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    return render(request, "food/confirm-delete.html", {"item": item})
