from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Questao

# Create your views here.

# request é a tentativa de acessar a página
def index(request):
    ultimas_perguntas_lista = Questao.objects.order_by('-pub_data')[:5]
    conteudo = {'ultimas_perguntas_lista':ultimas_perguntas_lista}
    # O que vai aparecer na página
    return render(request,'votar/index.html',conteudo)
    # renderiza uma página
    #return HttpResponse('Olá este é meu segundo site com Django')

#def detalhe(request,questao_id):
#    return HttpResponse(f'Essa é a pergunta de número {questao_id}')

def resultados(request,questao_id):
    questao = Questao(pk=questao_id)
    return render(request,'votar/resultados.html',{'questao':questao})
    #return HttpResponse(f'Esses são os resultados da pergunta de número {questao_id}')

def vote(request,questao_id):
    questao = get_object_or_404(Questao,pk=questao_id)

    try:
        escolha_selecionada = questao.escolha_set.get(pk=request.POST['escolha'])
    except KeyError:
        return render(request,'votar/vote.html',{
            'questao':questao,
            'mensagem_erro':'Você ainda não selecionou uma opção.'
        })
    else:
        escolha_selecionada.votos += 1
        escolha_selecionada.save()
        return HttpResponseRedirect(reverse('votar:resultados',args=(questao.id,)))
    #return HttpResponse(f'Você está votando na pergunta de número {questao_id}')