from django import template


register = template.plants()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity