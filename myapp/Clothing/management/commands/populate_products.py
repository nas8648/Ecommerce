from typing import Any
from django.core.management.base import BaseCommand
from Clothing.models import Product

class Command(BaseCommand):
    help = "Insert sample product data"

    def handle(self, *args: Any, **options: Any):

        names = [
            "Men Shirt 1", "Men Shirt 2", "Men Shirt 3", "Men Shirt 4", "Men Shirt 5", "Men Shirt 6",
            "Women Dress 1", "Women Dress 2", "Women Dress 3", "Women Dress 4", "Women Dress 5", "Women Dress 6",
            "Kid Outfit 1", "Kid Outfit 2", "Kid Outfit 3", "Kid Outfit 4", "Kid Outfit 5", "Kid Outfit 6"
        ]

        descriptions = [
            "Comfortable and stylish shirt for men.", "Premium cotton shirt for men.", "Casual shirt perfect for daily wear.",
            "Formal men shirt for office.", "Men shirt with modern design.", "Classic men shirt in various colors.",
            "Elegant dress for women.", "Casual dress for everyday.", "Summer dress with vibrant colors.",
            "Party wear dress for women.", "Office friendly women dress.", "Comfortable and stylish dress.",
            "Cute outfit for kids.", "Fun and playful kids outfit.", "Comfortable kids clothing.",
            "Kids outfit for school and play.", "Stylish kids clothes.", "Durable kids outfit."
        ]

        categories = [
            "Men", "Men", "Men", "Men", "Men", "Men",
            "Women", "Women", "Women", "Women", "Women", "Women",
            "Kid", "Kid", "Kid", "Kid", "Kid", "Kid"
        ]

        prices = [
            599, 649, 699, 549, 599, 629,
            799, 849, 899, 949, 799, 899,
            399, 449, 499, 459, 429, 479
        ]

        images = [
            "men1.jpg", "men2.jpg", "men3.jpg", "men4.jpg", "men5.jpg", "men6.jpg",
            "women1.jpg", "women2.jpg", "women3.jpg", "women4.jpg", "women5.jpg", "women6.jpg",
            "kid1.jpg", "kid2.jpg", "kid3.jpg", "kid4.jpg", "kid5.jpg", "kid6.jpg",
        ]

        # Optional: Clear old products
        Product.objects.all().delete()

        # Correct variable name in the loop
        for name, description, category, price, image in zip(names, descriptions, categories, prices, images):
            Product.objects.create(
                name=name,
                description=description,
                category=category,
                price=price,
                image=image
            )

        self.stdout.write(self.style.SUCCESS("✔ Sample Products Inserted"))
