from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse



from .models import list_item

def index(request):
    list_items = list_item.objects.all()
    return render(request, 'index.html', {'list_items': list_items})

class WishCreate(CreateView):
    model = list_item
    fields = '__all__'
    success_url = '/'


class WishDelete(DeleteView):  
    model = list_item

    def get_success_url(self):
        return reverse('index')  
      
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)