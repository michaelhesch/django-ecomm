from .cart import Cart


# Makes the cart available for all templates
# Instead of doing this in each view and passing to the template
def cart(request):
    return {'cart': Cart(request)}
