from orders.models import Order


def get_or_create_order(cart, request):
    order = Order.objects.filter(cart=cart).first()

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
        request.session['order_id'] = order.id

    if order:
        request.session['order_id'] = order.id

    return order
