from django.forms import ModelForm
from .models import Endereco, Cliente,	Produto, Pedido


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'