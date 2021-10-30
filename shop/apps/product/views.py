import random

from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_product = list(product.category.products.exclude(id=product.id))

    if len(similar_product) >= 4:
        similar_product = random.sample(similar_product, 4)
    
    return render(request, 'product/product.html', {'product': product, 'similar_product': similar_product})
