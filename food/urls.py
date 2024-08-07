from django.urls import path
from . import views
#from .views import IndexClassView
app_name = "food"
urlpatterns = [
    #path("", views.index, name="index"), Replaced with CBV Below
    path("", views.IndexClassView.as_view(), name="index"),
    path("detail/<int:pk>", views.FoodDetail.as_view(), name="detail"),
    # add item
    path("create_item/", views.create_item, name="create_item"),
    # update item
    path("update_item/<int:item_id>", views.update_item, name="update_item"),
    # delete item
    path("delete_item/<int:item_id>", views.delete_item, name="delete_item"),
]
