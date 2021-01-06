from django.shortcuts import render, get_object_or_404
from .models import Endereco, Cliente,	Produto, Pedido
#from .forms import EnderecoForm


# Create your views here.
def index(request):
	return render(request, 'core/index.html')


def cliente_list(request):
    cliente = Cliente.objects.all()
    #form = ClienteForm()
    #data = {'cliente': cliente, 'form': form}
    context = {'cliente': cliente}
    return render(request, 'core/cliente_list.html', context)
	



