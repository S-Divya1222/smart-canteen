import os
import re
import zipfile
import requests

OUTPUT_FOLDER = "food_images"
ZIP_NAME = "smart_canteen_food_images.zip"

FOODS = {
    "Idli": "Idli",
    "Sambar Idli": "Idli sambar",
    "Masala Dosa": "Masala dosa",
    "Plain Dosa": "Dosa",
    "Ghee Dosa": "Ghee dosa",
    "Pongal": "Ven pongal",
    "Poori Masala": "Puri bhaji",
    "Vada": "Medu vada",
    "Chapathi": "Chapati",
    "Upma": "Upma",

    "Chicken Biriyani": "Chicken biryani",
    "Mutton Biriyani": "Mutton biryani",
    "Egg Biriyani": "Egg biryani",
    "Veg Biriyani": "Vegetable biryani",
    "Chicken Rice": "Chicken fried rice",
    "Veg Fried Rice": "Fried rice",
    "Lemon Rice": "Lemon rice",
    "Tomato Rice": "Tomato rice",
    "Curd Rice": "Curd rice",
    "Sambar Rice": "Sambar rice",
    "South Indian Meals": "South Indian meals",
    "Mini Meals": "South Indian thali",

    "Plain Parotta": "Parotta",
    "Kothu Parotta": "Kothu parotta",
    "Egg Kothu Parotta": "Egg kothu parotta",
    "Chicken Kothu Parotta": "Chicken kothu parotta",
    "Chicken Noodles": "Chicken noodles",
    "Veg Noodles": "Noodles",
    "Chicken Fried Rice": "Chicken fried rice",
    "Egg Fried Rice": "Egg fried rice",
    "Dosa": "Dosa",

    "Samosa": "Samosa",
    "Vegetable Bajji": "Pakora",
    "Onion Bajji": "Onion bhaji",
    "Vada": "Vada",
    "Masala Vada": "Masala vada",
    "French Fries": "French fries",
    "Chicken 65": "Chicken 65",
    "Chicken Popcorn": "Chicken nuggets",
    "Sandwich": "Sandwich",
    "Veg Roll": "Vegetable roll",
    "Egg Puff": "Egg puff",
    "Chicken Puff": "Chicken puff",

    "Tea": "Masala chai",
    "Coffee": "Coffee",
    "Lemon Tea": "Lemon tea",
    "Fresh Lime": "Lime juice",
    "Orange Juice": "Orange juice",
    "Watermelon Juice": "Watermelon juice",
    "Mango Juice": "Mango juice",
    "Chocolate Milkshake": "Chocolate milkshake",
    "Strawberry Milkshake": "Strawberry milkshake",
    "Badam Milk": "Badam milk",

    "Vanilla Ice Cream": "Vanilla ice cream",
    "Chocolate Ice Cream": "Chocolate ice cream",
    "Strawberry Ice Cream": "Strawberry ice cream",
    "Gulab Jamun": "Gulab jamun",
    "Brownie": "Brownie",
    "Fruit Salad": "Fruit salad",
    "Payasam": "Payasam",
    "Caramel Custard": "Crème caramel",

    "Breakfast Combo": "Indian breakfast",
    "Biriyani Combo": "Biryani meal",
    "Chicken Rice Combo": "Chicken rice meal",
    "Parotta Combo": "Parotta meal",
    "Snacks Combo": "Indian snacks",
    "Student Special Combo": "Indian thali",
}


def clean_name(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_") + ".jpg"


def search_wikimedia(query):
    url = "https://commons.wikimedia.org/w/api.php"

    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,
        "gsrlimit": 5,
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": 800,
        "format": "json"
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "SmartCanteen/1.0"
        },
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    pages = data.get("query", {}).get("pages", {})

    for page in pages.values():

        imageinfo = page.get("imageinfo")

        if not imageinfo:
            continue

        image_url = (
            imageinfo[0].get("thumburl")
            or imageinfo[0].get("url")
        )

        if image_url:
            return image_url

    return None


def download_image(food_name, search_name):

    print()
    print("Searching:", food_name)

    try:

        image_url = search_wikimedia(search_name)

        if not image_url:
            print("❌ No image found")
            return False

        print("Found:", image_url)

        response = requests.get(
            image_url,
            headers={
                "User-Agent": "SmartCanteen/1.0"
            },
            timeout=30
        )

        response.raise_for_status()

        filename = clean_name(food_name)

        filepath = os.path.join(
            OUTPUT_FOLDER,
            filename
        )

        with open(filepath, "wb") as file:
            file.write(response.content)

        print("✅ Saved:", filename)

        return True

    except Exception as error:

        print("❌ Error:", error)

        return False


def main():

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    success = 0
    failed = []

    print()
    print("=" * 60)
    print(" SMART CANTEEN FOOD IMAGE DOWNLOADER")
    print("=" * 60)

    for food_name, search_name in FOODS.items():

        if download_image(
            food_name,
            search_name
        ):

            success += 1

        else:

            failed.append(food_name)

    print()
    print("=" * 60)
    print(" CREATING ZIP FILE")
    print("=" * 60)

    with zipfile.ZipFile(
        ZIP_NAME,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        for filename in os.listdir(OUTPUT_FOLDER):

            filepath = os.path.join(
                OUTPUT_FOLDER,
                filename
            )

            if os.path.isfile(filepath):

                zip_file.write(
                    filepath,
                    arcname=filename
                )

    print()
    print("✅ ZIP CREATED")
    print("File:", ZIP_NAME)
    print("Successful:", success)
    print("Failed:", len(failed))

    if failed:

        print()
        print("Images not found:")

        for item in failed:
            print("-", item)

    print()
    print("Done!")


if __name__ == "__main__":
    main()