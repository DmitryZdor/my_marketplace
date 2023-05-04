from products.models import ShoppingCart


def shopping_carts(request):
    user = request.user
    return {'shopping_carts': ShoppingCart.objects.filter(user=user) if user.is_authenticated else []}
