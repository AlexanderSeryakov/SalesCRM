from django import template

register = template.Library()


@register.filter(name='phone_format')
def phonenumber(number):
    return '{}-({})-{}-{}-{}'.format(number[0], number[1:4], number[4:7], number[7:9], number[9:11])


register.filter("phonenumber", phonenumber)
