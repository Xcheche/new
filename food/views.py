from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required # for function based views
from food.forms import ItemForm # importing the form
from food.models import Item # importing the model
from django.contrib.auth.mixins import LoginRequiredMixin # for class based views
from django.views.generic import ListView, DetailView # CBV ListView



# Create your views here.
# @login_required
# def index(request):
#     item_list = Item.objects.all()

#     context = {"item_list": item_list}
#     return render(request, "food/index.html", context) replaced with CBV Below


class IndexClassView(ListView, LoginRequiredMixin): # inheritance ListView and LoginRequiredMixin
    model = Item  # model
    template_name = "food/index.html" #template
    context_object_name = "item_list" #context variable

# @login_required Replacing with CBV
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)  # Fetch single item
#     context = {"item": item}
#     return render(request, "food/detail.html", context)

class FoodDetail(DetailView):
    model = Item
    template_name = "food/detail.html"

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
