from django.urls import path
from .views import add_product, product_details, edit_product, update_product, add_category, update_category,\
    all_category, edit_category

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/edit/<int:id>", edit_product, name="edit_product"),
    path("/update/<int:id>", update_product, name="update_product"),
    path("/category", all_category, name="all_category"),
    path("/category/add", add_category, name="add_category"),
    path("/category/update/<int:id>", update_category, name="update_category"),
    path("/category/edit/<int:id>", edit_category, name="edit_category"),
    path("/<int:id>", product_details, name="product_details")
]