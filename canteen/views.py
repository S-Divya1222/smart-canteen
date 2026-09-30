from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Order, OrderItem, FoodItem
# ==================================================
# HOME
# ==================================================

def home(request):
    return render(request, "home.html")

# ==================================================
# MENU
# ==================================================

def menu(request):
    foods = FoodItem.objects.filter(available=True)
    return render(request, 'menu.html', {'foods': foods})


# ==================================================
# ADD TO CART
# ==================================================

def add_to_cart(request, food_id):

    food = get_object_or_404(
        FoodItem,
        id=food_id,
        available=True
    )

    cart = request.session.get(
        "cart",
        {}
    )

    food_id = str(food_id)

    if food_id in cart:

        cart[food_id]["quantity"] += 1

    else:

        cart[food_id] = {
            "name": food.name,
            "price": float(food.price),
            "quantity": 1,
        }

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("menu")


# ==================================================
# CART
# ==================================================

def cart(request):

    session_cart = request.session.get(
        "cart",
        {}
    )

    cart_items = []
    total_price = 0
    total_items = 0

    for food_id, item in session_cart.items():

        quantity = int(
            item.get(
                "quantity",
                1
            )
        )

        price = float(
            item.get(
                "price",
                0
            )
        )

        item_total = price * quantity

        cart_items.append({
            "food_id": food_id,
            "name": item.get("name"),
            "price": price,
            "quantity": quantity,
            "item_total": item_total,
        })

        total_price += item_total
        total_items += quantity

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "total_price": total_price,
            "total_items": total_items,
        }
    )


# ==================================================
# REMOVE FROM CART
# ==================================================

def remove_from_cart(request, food_id):

    cart = request.session.get(
        "cart",
        {}
    )

    food_id = str(food_id)

    if food_id in cart:

        del cart[food_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# ==================================================
# INCREASE QUANTITY
# ==================================================

def increase_quantity(request, food_id):

    cart = request.session.get(
        "cart",
        {}
    )

    food_id = str(food_id)

    if food_id in cart:

        cart[food_id]["quantity"] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# ==================================================
# DECREASE QUANTITY
# ==================================================

def decrease_quantity(request, food_id):

    cart = request.session.get(
        "cart",
        {}
    )

    food_id = str(food_id)

    if food_id in cart:

        cart[food_id]["quantity"] -= 1

        if cart[food_id]["quantity"] <= 0:

            del cart[food_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# ==================================================
# CHECKOUT
# ==================================================

def checkout(request):

    session_cart = request.session.get(
        "cart",
        {}
    )

    cart_items = []
    total_price = 0

    for food_id, item in session_cart.items():

        quantity = int(
            item.get(
                "quantity",
                1
            )
        )

        price = float(
            item.get(
                "price",
                0
            )
        )

        item_total = price * quantity

        cart_items.append({
            "food_id": food_id,
            "name": item.get("name"),
            "price": price,
            "quantity": quantity,
            "item_total": item_total,
        })

        total_price += item_total

    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items,
            "total_price": total_price,
        }
    )


# ==================================================
# PLACE ORDER
# ==================================================

def place_order(request):

    if request.method != "POST":

        return redirect("checkout")

    student_name = request.POST.get(
        "student_name"
    )

    register_number = request.POST.get(
        "register_number"
    )

    phone_number = request.POST.get(
        "phone_number"
    )

    # ------------------------------------------
    # VALIDATE STUDENT DETAILS
    # ------------------------------------------

    if (
        not student_name
        or not register_number
        or not phone_number
    ):

        return render(
            request,
            "checkout.html",
            {
                "error":
                "Please fill all student details."
            }
        )

    # ------------------------------------------
    # GET CART
    # ------------------------------------------

    cart = request.session.get(
        "cart",
        {}
    )

    if not cart:

        return render(
            request,
            "checkout.html",
            {
                "error":
                "Your cart is empty."
            }
        )

    # ------------------------------------------
    # CALCULATE TOTAL
    # ------------------------------------------

    total_price = 0
    cart_items = []

    for food_id, item in cart.items():

        try:

            quantity = int(
                item.get(
                    "quantity",
                    1
                )
            )

            price = float(
                item.get(
                    "price",
                    0
                )
            )

        except (
            ValueError,
            TypeError
        ):

            continue

        item_total = price * quantity

        total_price += item_total

        cart_items.append({
            "food_id": food_id,
            "name": item.get("name"),
            "price": price,
            "quantity": quantity,
            "item_total": item_total,
        })

    if not cart_items:

        return render(
            request,
            "checkout.html",
            {
                "error":
                "Your cart is empty."
            }
        )

    # ------------------------------------------
    # CREATE ORDER
    # ------------------------------------------

    order = Order.objects.create(

        student_name=student_name,

        register_number=register_number,

        phone_number=phone_number,

        total_price=total_price,

        status="Pending"

    )

    # ------------------------------------------
    # SAVE ORDER ITEMS
    # ------------------------------------------

    for item in cart_items:

        food = get_object_or_404(
            FoodItem,
            id=item["food_id"]
        )

        OrderItem.objects.create(

            order=order,

            food=food,

            quantity=item["quantity"],

            price=item["price"]

        )

    # ------------------------------------------
    # CLEAR CART
    # ------------------------------------------

    request.session["cart"] = {}
    request.session.modified = True

    # ------------------------------------------
    # ORDER SUCCESS
    # ------------------------------------------

    return render(
        request,
        "order_success.html",
        {
            "order": order
        }
    )


# ==================================================
# ADMIN ORDER MANAGEMENT
# ==================================================

# ==================================================
# ADMIN ORDER MANAGEMENT
# ==================================================


@login_required
def admin_orders(request):

    orders = Order.objects.all().prefetch_related(
        "items__food"
    ).order_by("-order_date")

    search = request.GET.get("search", "").strip()
    status_filter = request.GET.get("status", "").strip()

    # Search
    if search:
        orders = orders.filter(
            models.Q(student_name__icontains=search) |
            models.Q(register_number__icontains=search) |
            models.Q(phone_number__icontains=search)
        )

    # Status filter
    if status_filter:
        orders = orders.filter(
            status=status_filter
        )

    # Dashboard counts
    total_count = Order.objects.count()

    pending_count = Order.objects.filter(
        status="Pending"
    ).count()

    preparing_count = Order.objects.filter(
        status="Preparing"
    ).count()

    ready_count = Order.objects.filter(
        status="Ready"
    ).count()

    completed_count = Order.objects.filter(
        status="Completed"
    ).count()

    cancelled_count = Order.objects.filter(
        status="Cancelled"
    ).count()

    return render(
        request,
        "admin_orders.html",
        {
            "orders": orders,
            "total_count": total_count,
            "pending_count": pending_count,
            "preparing_count": preparing_count,
            "ready_count": ready_count,
            "completed_count": completed_count,
            "cancelled_count": cancelled_count,
            "status_choices": Order.STATUS_CHOICES,
            "search": search,
            "status_filter": status_filter,
        }
    )
# ==================================================
# UPDATE ORDER STATUS
# ==================================================

@login_required
def update_order_status(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    if request.method == "POST":

        new_status = request.POST.get(
            "status"
        )

        valid_statuses = dict(
            Order.STATUS_CHOICES
        )

        if new_status in valid_statuses:

            order.status = new_status

            order.save()

    return redirect(
        "admin_orders"
    )


# ==================================================
# STUDENT ORDER TRACKING
# ==================================================

# ==================================================
# STUDENT ORDER TRACKING
# ==================================================

def my_orders(request):

    orders = None
    searched = False
    error = None

    if request.method == "POST":

        register_number = request.POST.get(
            "register_number",
            ""
        ).strip()

        phone_number = request.POST.get(
            "phone_number",
            ""
        ).strip()

        searched = True

        # --------------------------------------
        # NO DETAILS
        # --------------------------------------

        if not register_number and not phone_number:

            error = (
                "Please enter Register Number "
                "or Phone Number."
            )

        # --------------------------------------
        # BOTH DETAILS
        # --------------------------------------

        elif register_number and phone_number:

            orders = Order.objects.filter(
                register_number=register_number,
                phone_number=phone_number
            ).prefetch_related(
                "items__food"
            ).order_by(
                "-order_date"
            )

        # --------------------------------------
        # REGISTER NUMBER ONLY
        # --------------------------------------

        elif register_number:

            orders = Order.objects.filter(
                register_number=register_number
            ).prefetch_related(
                "items__food"
            ).order_by(
                "-order_date"
            )

        # --------------------------------------
        # PHONE NUMBER ONLY
        # --------------------------------------

        else:

            orders = Order.objects.filter(
                phone_number=phone_number
            ).prefetch_related(
                "items__food"
            ).order_by(
                "-order_date"
            )

    return render(
    request,
    "canteen/my_orders.html",
    {
        "orders": orders,
        "searched": searched,
        "error": error,
        "register_number": register_number if request.method == "POST" else "",
        "phone_number": phone_number if request.method == "POST" else "",
    }
)