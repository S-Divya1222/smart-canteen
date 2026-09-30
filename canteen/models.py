from django.db import models


class FoodItem(models.Model):

    CATEGORY_CHOICES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Snacks", "Snacks"),
        ("Drinks", "Drinks"),
        ("Cool Drinks", "Cool Drinks"),
        ("Desserts", "Desserts"),
        ("Combos", "Combos"),
        ("Main Food", "Main Food"),
        ("Side Dishes", "Side Dishes"),
    ]

    name = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="food/",
        blank=True,
        null=True
    )

    available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    student_name = models.CharField(
        max_length=100,
        default="Unknown"
    )

    register_number = models.CharField(
        max_length=50,
        default="Unknown"
    )

    phone_number = models.CharField(
        max_length=15,
        default="Unknown"
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    order_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student_name} - {self.register_number}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    food = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    @property
    def total_item_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.food.name} x {self.quantity}"