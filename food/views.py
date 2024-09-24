from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy  # for function based views
from food.forms import ItemForm  # importing the form
from food.models import Item  # importing the model
from django.contrib.auth.mixins import LoginRequiredMixin  # for class based views
from django.views.generic import ListView, DetailView, CreateView  # CBV ListView


# Create your views here.
# @login_required
# def index(request):
#     item_list = Item.objects.all()

#     context = {"item_list": item_list}
#     return render(request, "food/index.html", context) replaced with CBV Below


class IndexClassView(
    LoginRequiredMixin, ListView
):  # inheritance ListView and LoginRequiredMixin
    model = Item  # model
    template_name = "food/index.html"  # template
    context_object_name = "item_list"  # context variable


# @login_required Replacing with CBV
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)  # Fetch single item
#     context = {"item": item}
#     return render(request, "food/detail.html", context)


class FoodDetail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "food/detail.html"
    context_object_name = "item"


# @login_required
# def create_item(request): converted to cbv

#     if request.method == "POST":
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("food:index")
#     else:
#         form = ItemForm()


#     return render(request, "food/item-form.html", {"form": form})
class CreateItem(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "food/item-form.html"
    fields = ["item_name", "item_desc", "item_price", "item_image", "user_name"]
    success_url = reverse_lazy("food:index")

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        messages.success(self.request, "Item added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error adding the item. Please try again."
        )
        return super().form_invalid(form)


@login_required
def update(request, item_id):

    item = item = get_object_or_404(Item, pk=item_id)

    if request.method == "POST":
        form = ItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse("food:index"))
    else:
        form = ItemForm(instance=item)
        context = {
            "form": form,
            "item": item,
        }

    return render(request, "food/update.html", context)


@login_required
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    return render(request, "food/confirm-delete.html", {"item": item})
