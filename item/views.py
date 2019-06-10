from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ItemForm


@login_required
def index(request):
    items = Item.objects.filter(owner=request.user).order_by('deadline')
    context = {
        'title': "Todo List",
        'items': items
    }
    return render(request, 'item/index.html', context)


@login_required
def details(request, id):
    item = Item.objects.get(id=id)
    if item.owner != request.user:
        raise Http404
    context = {
        'item': item
    }
    return render(request, 'item/details.html', context)


@login_required
def newItem(request):
    if request.method != 'POST':
        form = ItemForm
    else:
        form = ItemForm(data=request.POST)
        if form.is_valid():
            newItem = form.save(commit=False)
            newItem.owner = request.user
            newItem.save()
            return HttpResponseRedirect(reverse('item:index'))

    context = {'form': form}
    return render(request, 'item/newItem.html', context)


@login_required
def completeItem(request, id):
    item = Item.objects.get(id=id)
    item.isComplete = True
    item.save()
    return HttpResponseRedirect(reverse('item:index'))


@login_required
def deleteItem(request, id):
    Item.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('item:index'))


@login_required
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
