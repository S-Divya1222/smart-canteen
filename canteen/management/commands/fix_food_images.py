import os

from django.conf import settings
from django.core.management.base import BaseCommand

from canteen.models import FoodItem


def image_filename(name):
    return name.strip().lower().replace(" ", "_").replace("-", "_") + ".jpg"


class Command(BaseCommand):
    help = "Point every FoodItem at its local image in media/food/"

    def handle(self, *args, **options):
        fixed = ok = missing = 0

        for food in FoodItem.objects.all():
            filename = image_filename(food.name)
            relative = f"food/{filename}"
            full_path = os.path.join(settings.MEDIA_ROOT, "food", filename)

            if not os.path.exists(full_path):
                missing += 1
                self.stdout.write(self.style.WARNING(f"No image file for: {food.name} ({filename})"))
                continue

            if food.image.name != relative:
                food.image = relative
                food.save(update_fields=["image"])
                fixed += 1
            else:
                ok += 1

        self.stdout.write(self.style.SUCCESS(
            f"Images fixed: {fixed} | already correct: {ok} | missing files: {missing}"
        ))
