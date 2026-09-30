from django.urls import path
from . import views


urlpatterns = [

    # HOME
    path(
        "",
        views.home,
        name="home"
    ),

    # MENU
    path(
        "menu/",
        views.menu,
        name="menu"
    ),

    # ADD TO CART
    path(
        "add-to-cart/<int:food_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    # CART
    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    # INCREASE
    path(
        "increase/<int:food_id>/",
        views.increase_quantity,
        name="increase_quantity"
    ),

    # DECREASE
    path(
        "decrease/<int:food_id>/",
        views.decrease_quantity,
        name="decrease_quantity"
    ),

    # REMOVE
    path(
        "remove/<int:food_id>/",
        views.remove_from_cart,
        name="remove_from_cart"
    ),

    # CHECKOUT
    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    # PLACE ORDER
    path(
        "place-order/",
        views.place_order,
        name="place_order"
    ),

    # ADMIN ORDERS
    path(
        "admin-orders/",
        views.admin_orders,
        name="admin_orders"
    ),

    # UPDATE STATUS
    path(
        "update-order-status/<int:order_id>/",
        views.update_order_status,
        name="update_order_status"
    ),

    # TRACK ORDER
    path(
        "my-orders/",
        views.my_orders,
        name="my_orders"
    ),
]