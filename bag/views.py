from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from plants.models import Plants
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, plants_id):
    """ Add a quantity of the specified product to the shopping bag """

    plants = get_object_or_404(Plants, pk=plants_id)
    quantity = 1
    redirect_url = 'plants'

    bag = request.session.get('bag', {})

    if plants_id in list(bag.keys()):
        bag[plants_id] += quantity
        messages.success(
            request, f'{plants.name} has been added to your plants bag again')
    else:
        bag[plants_id] = quantity
        messages.success(request, f'Added {plants.name} to your plants bag')

    request.session['bag'] = bag
    print('bag contents:', bag)
    return redirect(redirect_url)


def adjust_bag(request, plants_id):
    """ adjust the quantity of the specified product to the specified amount """

    plants = get_object_or_404(Plants, pk=plants_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[plant_id] = quantity
        messages.success(
            request, f'Updated the quantity of {plants.title} plants in your plant bag')
    else:
        bag.pop(plants_id)
        messages.success(request, f'Removed {plant.title} from your plant bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, plant_id):
    """ remove item from the shopping bag """

    try:
        plant = get_object_or_404(Plants, pk=plant_id)
        bag = request.session.get('bag', {})

        bag.pop(plant_id)
        messages.success(request, f'Removed {plant.title} from your plant bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)