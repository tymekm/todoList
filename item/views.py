from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ItemForm


def index(request):
    items = Item.objects.all()
    context = {
        'title': "Todo List",
        'items': items
    }
    return render(request, 'item/index.html', context)


def details(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'item/details.html', context)


def newItem(request):
    if request.method != 'POST':
        form = ItemForm
    else:
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item:index'))

    context = {'form': form}
    return render(request, 'item/newItem.html', context)


def editItem(request, id):
    item = Item.objects.get(id=id)

    if request.method != 'POST':
        form = ItemForm(instance=item)
    else:
        form = ItemForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item:index'))

    context = {'item': item, 'form': form}
    return render(request, 'item/editItem.html', context)
