from django.shortcuts import render
from testapp.forms import AddItemForm

# Create your views here.
def index_view(request):

    return render(request,'testapp/home.html')


def add_item_view(request):
    form = AddItemForm()
    response = render(request,'testapp/additem.html',{'form':form})

    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response

def display_items_view(request):

    return render(request,'testapp/diplayitems.html')
