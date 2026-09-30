from PIL import Image, ImageDraw, ImageFont
import os
import zipfile
import re

OUTPUT = "food_images"

FOODS = [
    "Idli",
    "Sambar Idli",
    "Masala Dosa",
    "Plain Dosa",
    "Ghee Dosa",
    "Pongal",
    "Poori Masala",
    "Vada",
    "Chapathi",
    "Upma",

    "Chicken Biriyani",
    "Mutton Biriyani",
    "Egg Biriyani",
    "Veg Biriyani",
    "Chicken Rice",
    "Veg Fried Rice",
    "Lemon Rice",
    "Tomato Rice",
    "Curd Rice",
    "Sambar Rice",
    "South Indian Meals",
    "Mini Meals",

    "Plain Parotta",
    "Kothu Parotta",
    "Egg Kothu Parotta",
    "Chicken Kothu Parotta",
    "Chicken Noodles",
    "Veg Noodles",
    "Chicken Fried Rice",
    "Egg Fried Rice",
    "Dosa",

    "Samosa",
    "Vegetable Bajji",
    "Onion Bajji",
    "Masala Vada",
    "French Fries",
    "Chicken 65",
    "Chicken Popcorn",
    "Sandwich",
    "Veg Roll",
    "Egg Puff",
    "Chicken Puff",

    "Tea",
    "Coffee",
    "Lemon Tea",
    "Fresh Lime",
    "Orange Juice",
    "Watermelon Juice",
    "Mango Juice",
    "Chocolate Milkshake",
    "Strawberry Milkshake",
    "Badam Milk",

    "Vanilla Ice Cream",
    "Chocolate Ice Cream",
    "Strawberry Ice Cream",
    "Gulab Jamun",
    "Brownie",
    "Fruit Salad",
    "Payasam",
    "Caramel Custard",

    "Breakfast Combo",
    "Biriyani Combo",
    "Chicken Rice Combo",
    "Parotta Combo",
    "Snacks Combo",
    "Student Special Combo",
]


def filename(name):
    return re.sub(
        r"[^a-z0-9]+",
        "_",
        name.lower()
    ).strip("_") + ".jpg"


def create_image(name, number):

    width = 900
    height = 650

    image = Image.new(
        "RGB",
        (width, height),
        (245, 238, 220)
    )

    draw = ImageDraw.Draw(image)

    # Food-card style background
    draw.rounded_rectangle(
        (30, 30, 870, 620),
        radius=35,
        fill=(255, 250, 240)
    )

    # Large food illustration area
    draw.ellipse(
        (170, 90, 730, 470),
        fill=(235, 220, 190)
    )

    # Decorative plate
    draw.ellipse(
        (220, 140, 680, 420),
        fill=(250, 250, 245),
        outline=(210, 190, 160),
        width=8
    )

    # Food-style colored center
    food_colors = [
        (190, 120, 55),
        (220, 150, 60),
        (170, 90, 45),
        (210, 180, 80),
        (120, 150, 75),
        (200, 100, 80),
    ]

    color = food_colors[number % len(food_colors)]

    draw.ellipse(
        (315, 210, 585, 380),
        fill=color
    )

    # Small food pieces
    for i in range(6):

        x = 300 + (i * 55)
        y = 250 + ((i % 2) * 55)

        draw.ellipse(
            (x, y, x + 45, y + 35),
            fill=food_colors[
                (number + i) % len(food_colors)
            ]
        )

    # Font
    try:
        font_large = ImageFont.truetype(
            "arial.ttf",
            48
        )

        font_small = ImageFont.truetype(
            "arial.ttf",
            28
        )

    except:

        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Food name
    bbox = draw.textbbox(
        (0, 0),
        name,
        font=font_large
    )

    text_width = bbox[2] - bbox[0]

    draw.text(
        (
            (width - text_width) / 2,
            495
        ),
        name,
        fill=(55, 45, 35),
        font=font_large
    )

    # Smart Canteen label
    draw.text(
        (30, 570),
        "Smart Canteen",
        fill=(110, 90, 70),
        font=font_small
    )

    return image


def main():

    os.makedirs(
        OUTPUT,
        exist_ok=True
    )

    print()
    print("=" * 60)
    print("SMART CANTEEN IMAGE GENERATOR")
    print("=" * 60)

    for number, food in enumerate(FOODS):

        file = filename(food)

        path = os.path.join(
            OUTPUT,
            file
        )

        image = create_image(
            food,
            number
        )

        image.save(
            path,
            "JPEG",
            quality=92
        )

        print("✅", file)

    zip_name = "smart_canteen_food_images.zip"

    with zipfile.ZipFile(
        zip_name,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        for file in os.listdir(OUTPUT):

            path = os.path.join(
                OUTPUT,
                file
            )

            if os.path.isfile(path):

                zip_file.write(
                    path,
                    arcname=file
                )

    print()
    print("=" * 60)
    print("✅ ZIP CREATED SUCCESSFULLY")
    print("=" * 60)
    print()
    print(zip_name)
    print()
    print("Total images:", len(FOODS))


if __name__ == "__main__":
    main()