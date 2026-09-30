from django.core.management.base import BaseCommand
from canteen.models import FoodItem


class Command(BaseCommand):

    help = "Create the 68 Smart Canteen menu items"

    def handle(self, *args, **kwargs):

        menu = [

            # ================= BREAKFAST =================

            {
                "name": "Idli",
                "category": "Breakfast",
                "description": "Soft and fluffy steamed idli",
                "price": 30,
                "image": "https://loremflickr.com/600/400/idli",
            },

            {
                "name": "Sambar Idli",
                "category": "Breakfast",
                "description": "Soft idli served with delicious sambar",
                "price": 40,
                "image": "https://loremflickr.com/600/400/idli,sambar",
            },

            {
                "name": "Masala Dosa",
                "category": "Breakfast",
                "description": "Crispy dosa with potato masala",
                "price": 60,
                "image": "https://loremflickr.com/600/400/masala,dosa",
            },

            {
                "name": "Plain Dosa",
                "category": "Breakfast",
                "description": "Crispy traditional South Indian dosa",
                "price": 45,
                "image": "https://loremflickr.com/600/400/dosa",
            },

            {
                "name": "Ghee Dosa",
                "category": "Breakfast",
                "description": "Crispy dosa roasted with ghee",
                "price": 65,
                "image": "https://loremflickr.com/600/400/ghee,dosa",
            },

            {
                "name": "Pongal",
                "category": "Breakfast",
                "description": "Hot and delicious South Indian pongal",
                "price": 45,
                "image": "https://loremflickr.com/600/400/pongal",
            },

            {
                "name": "Poori Masala",
                "category": "Breakfast",
                "description": "Fluffy poori served with potato masala",
                "price": 50,
                "image": "https://loremflickr.com/600/400/poori,masala",
            },

            {
                "name": "Vada",
                "category": "Breakfast",
                "description": "Crispy traditional South Indian vada",
                "price": 25,
                "image": "https://loremflickr.com/600/400/vada",
            },

            {
                "name": "Chapathi",
                "category": "Breakfast",
                "description": "Soft and fresh chapathi",
                "price": 35,
                "image": "https://loremflickr.com/600/400/chapathi",
            },

            {
                "name": "Upma",
                "category": "Breakfast",
                "description": "Traditional South Indian upma",
                "price": 35,
                "image": "https://loremflickr.com/600/400/upma",
            },


            # ================= LUNCH =================

            {
                "name": "Chicken Biriyani",
                "category": "Lunch",
                "description": "Flavorful chicken biriyani with aromatic spices",
                "price": 120,
                "image": "https://loremflickr.com/600/400/chicken,biriyani",
            },

            {
                "name": "Mutton Biriyani",
                "category": "Lunch",
                "description": "Rich and aromatic mutton biriyani",
                "price": 160,
                "image": "https://loremflickr.com/600/400/mutton,biriyani",
            },

            {
                "name": "Egg Biriyani",
                "category": "Lunch",
                "description": "Spiced biriyani served with egg",
                "price": 90,
                "image": "https://loremflickr.com/600/400/egg,biriyani",
            },

            {
                "name": "Veg Biriyani",
                "category": "Lunch",
                "description": "Fragrant vegetable biriyani",
                "price": 80,
                "image": "https://loremflickr.com/600/400/vegetable,biriyani",
            },

            {
                "name": "Chicken Rice",
                "category": "Lunch",
                "description": "Flavorful chicken fried rice",
                "price": 100,
                "image": "https://loremflickr.com/600/400/chicken,rice",
            },

            {
                "name": "Veg Fried Rice",
                "category": "Lunch",
                "description": "Fried rice with fresh vegetables",
                "price": 80,
                "image": "https://loremflickr.com/600/400/vegetable,fried,rice",
            },

            {
                "name": "Lemon Rice",
                "category": "Lunch",
                "description": "Tangy and flavorful lemon rice",
                "price": 50,
                "image": "https://loremflickr.com/600/400/lemon,rice",
            },

            {
                "name": "Tomato Rice",
                "category": "Lunch",
                "description": "Spicy and flavorful tomato rice",
                "price": 50,
                "image": "https://loremflickr.com/600/400/tomato,rice",
            },

            {
                "name": "Curd Rice",
                "category": "Lunch",
                "description": "Cool and creamy curd rice",
                "price": 45,
                "image": "https://loremflickr.com/600/400/curd,rice",
            },

            {
                "name": "Sambar Rice",
                "category": "Lunch",
                "description": "Rice mixed with tasty sambar",
                "price": 50,
                "image": "https://loremflickr.com/600/400/sambar,rice",
            },

            {
                "name": "South Indian Meals",
                "category": "Lunch",
                "description": "Complete traditional South Indian meal",
                "price": 100,
                "image": "https://loremflickr.com/600/400/south,indian,meals",
            },

            {
                "name": "Mini Meals",
                "category": "Lunch",
                "description": "Perfect portion meal for students",
                "price": 70,
                "image": "https://loremflickr.com/600/400/indian,meal",
            },


            # ================= DINNER =================

            {
                "name": "Plain Parotta",
                "category": "Dinner",
                "description": "Flaky and soft layered parotta",
                "price": 40,
                "image": "https://loremflickr.com/600/400/parotta",
            },

            {
                "name": "Kothu Parotta",
                "category": "Dinner",
                "description": "Chopped parotta cooked with spices",
                "price": 80,
                "image": "https://loremflickr.com/600/400/kothu,parotta",
            },

            {
                "name": "Egg Kothu Parotta",
                "category": "Dinner",
                "description": "Kothu parotta with egg",
                "price": 90,
                "image": "https://loremflickr.com/600/400/egg,kothu,parotta",
            },

            {
                "name": "Chicken Kothu Parotta",
                "category": "Dinner",
                "description": "Spicy chicken kothu parotta",
                "price": 120,
                "image": "https://loremflickr.com/600/400/chicken,kothu,parotta",
            },

            {
                "name": "Chapathi",
                "category": "Dinner",
                "description": "Soft homemade-style chapathi",
                "price": 35,
                "image": "https://loremflickr.com/600/400/chapathi",
            },

            {
                "name": "Chicken Noodles",
                "category": "Dinner",
                "description": "Spicy noodles with chicken",
                "price": 100,
                "image": "https://loremflickr.com/600/400/chicken,noodles",
            },

            {
                "name": "Veg Noodles",
                "category": "Dinner",
                "description": "Stir-fried noodles with vegetables",
                "price": 80,
                "image": "https://loremflickr.com/600/400/vegetable,noodles",
            },

            {
                "name": "Chicken Fried Rice",
                "category": "Dinner",
                "description": "Classic chicken fried rice",
                "price": 100,
                "image": "https://loremflickr.com/600/400/chicken,fried,rice",
            },

            {
                "name": "Egg Fried Rice",
                "category": "Dinner",
                "description": "Fried rice with scrambled egg",
                "price": 90,
                "image": "https://loremflickr.com/600/400/egg,fried,rice",
            },

            {
                "name": "Dosa",
                "category": "Dinner",
                "description": "Crispy traditional dosa",
                "price": 45,
                "image": "https://loremflickr.com/600/400/dosa",
            },


            # ================= SNACKS =================

            {
                "name": "Samosa",
                "category": "Snacks",
                "description": "Crispy golden samosa",
                "price": 20,
                "image": "https://loremflickr.com/600/400/samosa",
            },

            {
                "name": "Vegetable Bajji",
                "category": "Snacks",
                "description": "Crispy vegetable fritters",
                "price": 25,
                "image": "https://loremflickr.com/600/400/vegetable,bajji",
            },

            {
                "name": "Onion Bajji",
                "category": "Snacks",
                "description": "Crispy onion bajji",
                "price": 25,
                "image": "https://loremflickr.com/600/400/onion,bajji",
            },

            {
                "name": "Vada",
                "category": "Snacks",
                "description": "Crispy traditional vada",
                "price": 20,
                "image": "https://loremflickr.com/600/400/vada",
            },

            {
                "name": "Masala Vada",
                "category": "Snacks",
                "description": "Spicy crispy masala vada",
                "price": 25,
                "image": "https://loremflickr.com/600/400/masala,vada",
            },

            {
                "name": "French Fries",
                "category": "Snacks",
                "description": "Crispy golden French fries",
                "price": 50,
                "image": "https://loremflickr.com/600/400/french,fries",
            },

            {
                "name": "Chicken 65",
                "category": "Snacks",
                "description": "Spicy crispy chicken bites",
                "price": 100,
                "image": "https://loremflickr.com/600/400/chicken,65",
            },

            {
                "name": "Chicken Popcorn",
                "category": "Snacks",
                "description": "Crispy bite-sized chicken",
                "price": 90,
                "image": "https://loremflickr.com/600/400/chicken,popcorn",
            },

            {
                "name": "Sandwich",
                "category": "Snacks",
                "description": "Fresh and tasty sandwich",
                "price": 50,
                "image": "https://loremflickr.com/600/400/sandwich",
            },

            {
                "name": "Veg Roll",
                "category": "Snacks",
                "description": "Fresh vegetable stuffed roll",
                "price": 50,
                "image": "https://loremflickr.com/600/400/vegetable,roll",
            },

            {
                "name": "Egg Puff",
                "category": "Snacks",
                "description": "Flaky puff filled with egg",
                "price": 30,
                "image": "https://loremflickr.com/600/400/egg,puff",
            },

            {
                "name": "Chicken Puff",
                "category": "Snacks",
                "description": "Crispy puff with chicken filling",
                "price": 40,
                "image": "https://loremflickr.com/600/400/chicken,puff",
            },


            # ================= DRINKS =================

            {
                "name": "Tea",
                "category": "Drinks",
                "description": "Hot refreshing tea",
                "price": 15,
                "image": "https://loremflickr.com/600/400/tea",
            },

            {
                "name": "Coffee",
                "category": "Drinks",
                "description": "Hot aromatic coffee",
                "price": 20,
                "image": "https://loremflickr.com/600/400/coffee",
            },

            {
                "name": "Lemon Tea",
                "category": "Drinks",
                "description": "Refreshing lemon tea",
                "price": 20,
                "image": "https://loremflickr.com/600/400/lemon,tea",
            },

            {
                "name": "Fresh Lime",
                "category": "Drinks",
                "description": "Fresh and refreshing lime drink",
                "price": 30,
                "image": "https://loremflickr.com/600/400/fresh,lime",
            },

            {
                "name": "Orange Juice",
                "category": "Drinks",
                "description": "Fresh orange juice",
                "price": 50,
                "image": "https://loremflickr.com/600/400/orange,juice",
            },

            {
                "name": "Watermelon Juice",
                "category": "Drinks",
                "description": "Cool watermelon juice",
                "price": 50,
                "image": "https://loremflickr.com/600/400/watermelon,juice",
            },

            {
                "name": "Mango Juice",
                "category": "Drinks",
                "description": "Sweet and refreshing mango juice",
                "price": 60,
                "image": "https://loremflickr.com/600/400/mango,juice",
            },

            {
                "name": "Chocolate Milkshake",
                "category": "Drinks",
                "description": "Rich creamy chocolate milkshake",
                "price": 80,
                "image": "https://loremflickr.com/600/400/chocolate,milkshake",
            },

            {
                "name": "Strawberry Milkshake",
                "category": "Drinks",
                "description": "Creamy strawberry milkshake",
                "price": 80,
                "image": "https://loremflickr.com/600/400/strawberry,milkshake",
            },

            {
                "name": "Badam Milk",
                "category": "Drinks",
                "description": "Rich almond milk",
                "price": 60,
                "image": "https://loremflickr.com/600/400/badam,milk",
            },


            # ================= DESSERTS =================

            {
                "name": "Vanilla Ice Cream",
                "category": "Desserts",
                "description": "Creamy vanilla ice cream",
                "price": 50,
                "image": "https://loremflickr.com/600/400/vanilla,ice,cream",
            },

            {
                "name": "Chocolate Ice Cream",
                "category": "Desserts",
                "description": "Rich chocolate ice cream",
                "price": 50,
                "image": "https://loremflickr.com/600/400/chocolate,ice,cream",
            },

            {
                "name": "Strawberry Ice Cream",
                "category": "Desserts",
                "description": "Sweet strawberry ice cream",
                "price": 50,
                "image": "https://loremflickr.com/600/400/strawberry,ice,cream",
            },

            {
                "name": "Gulab Jamun",
                "category": "Desserts",
                "description": "Soft and sweet gulab jamun",
                "price": 40,
                "image": "https://loremflickr.com/600/400/gulab,jamun",
            },

            {
                "name": "Brownie",
                "category": "Desserts",
                "description": "Soft chocolate brownie",
                "price": 60,
                "image": "https://loremflickr.com/600/400/brownie",
            },

            {
                "name": "Fruit Salad",
                "category": "Desserts",
                "description": "Fresh mixed fruit salad",
                "price": 50,
                "image": "https://loremflickr.com/600/400/fruit,salad",
            },

            {
                "name": "Payasam",
                "category": "Desserts",
                "description": "Traditional creamy payasam",
                "price": 45,
                "image": "https://loremflickr.com/600/400/payasam",
            },

            {
                "name": "Caramel Custard",
                "category": "Desserts",
                "description": "Silky smooth caramel custard",
                "price": 60,
                "image": "https://loremflickr.com/600/400/caramel,custard",
            },


            # ================= COMBOS =================

            {
                "name": "Breakfast Combo",
                "category": "Combos",
                "description": "Idli + Vada + Sambar + Chutney",
                "price": 70,
                "image": "https://loremflickr.com/600/400/breakfast,indian",
            },

            {
                "name": "Biriyani Combo",
                "category": "Combos",
                "description": "Chicken Biriyani + Egg + Drink",
                "price": 150,
                "image": "https://loremflickr.com/600/400/biriyani,combo",
            },

            {
                "name": "Chicken Rice Combo",
                "category": "Combos",
                "description": "Chicken Rice + Egg + Drink",
                "price": 130,
                "image": "https://loremflickr.com/600/400/chicken,rice,combo",
            },

            {
                "name": "Parotta Combo",
                "category": "Combos",
                "description": "2 Parotta + Chicken Curry",
                "price": 110,
                "image": "https://loremflickr.com/600/400/parotta,combo",
            },

            {
                "name": "Snacks Combo",
                "category": "Combos",
                "description": "Samosa + Chicken Popcorn + Fresh Lime",
                "price": 120,
                "image": "https://loremflickr.com/600/400/snacks,combo",
            },

            {
                "name": "Student Special Combo",
                "category": "Combos",
                "description": "Rice + Side Dish + Drink + Dessert",
                "price": 130,
                "image": "https://loremflickr.com/600/400/student,meal",
            },
        ]


        created = 0
        updated = 0

        for item in menu:

            food, was_created = FoodItem.objects.update_or_create(
                name=item["name"],
                category=item["category"],
                defaults={
                    "description": item["description"],
                    "price": item["price"],
                    # Local file in media/food/ (e.g. "Masala Dosa" -> food/masala_dosa.jpg)
                    "image": "food/" + item["name"].strip().lower().replace(" ", "_").replace("-", "_") + ".jpg",
                    "available": True,
                }
            )

            if was_created:
                created += 1
            else:
                updated += 1


        self.stdout.write(
            self.style.SUCCESS(
                f"Menu setup completed!"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created: {created}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated: {updated}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Total menu items: {len(menu)}"
            )
        )