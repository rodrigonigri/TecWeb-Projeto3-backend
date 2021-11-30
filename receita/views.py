from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import ReceitaSerializer
from .models import Receita
from rest_framework import status

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

# GET
@api_view(['GET', 'POST', 'DELETE'])
def api_receita(request, receita_id):
    try:
        receita = Receita.objects.get(id=receita_id)
    except Receita.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_receita_data = request.data
        receita.title = new_receita_data['title']
        receita.content = new_receita_data['ingredients']
        receita.content = new_receita_data['preparo']
        receita.save()


    if request.method == 'DELETE':
        receita.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    serialized_receita = ReceitaSerializer(receita)
    return Response(serialized_receita.data)


#
@api_view(['GET','POST'])
def api_receita_list(request):

    if request.method == "POST":
        new_receita_data = request.data
        receita = Receita()
        receita.title = new_receita_data['title']
        receita.ingredients = new_receita_data['ingredients']
        receita.preparo = new_receita_data['preparo']
        receita.save()

    receitas = Receita.objects.all()
    serialized_receitas = ReceitaSerializer(receitas, many=True)
    return Response(serialized_receitas.data)

