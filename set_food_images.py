import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartcanteen.settings")

import django

django.setup()

from canteen.models import FoodItem


def image_filename(food_name):
    return (
        food_name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        + ".jpg"
    )


foods = FoodItem.objects.all()

success = 0
failed = 0

print()
print("=" * 60)
print("SMART CANTEEN - FOOD IMAGE ASSIGNMENT")
print("=" * 60)
print()

for food in foods:

    filename = image_filename(food.name)

    full_path = os.path.join(
        "media",
        "food",
        filename
    )

    print(f"Food: {food.name}")
    print(f"Image: {filename}")

    if os.path.exists(full_path):

        food.image = f"food/{filename}"
        food.save(update_fields=["image"])

        print("✅ ASSIGNED")
        success += 1

    else:

        print("❌ IMAGE NOT FOUND")
        failed += 1

    print()


print("=" * 60)
print("DONE")
print("=" * 60)
print(f"Successful: {success}")
print(f"Failed: {failed}")
print()