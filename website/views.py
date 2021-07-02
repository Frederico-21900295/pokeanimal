from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from matplotlib import pyplot as plt
from django.views.generic import ListView
from django.contrib.auth import login as auth_login

from website.forms import ContatoForm, ComentarioForm, SignUpForm
from website.models import Quizz, Pergunta, Nota, Pokedex, Resposta, Comentario, Comentario_values, Contato


def home_page_view(request) :
    return render(request, 'index.html')


def animais(request) :
    return render(request, 'animais.html')


def anfibios(request) :
    return render(request, 'anfibios.html')


def aves(request) :
    return render(request, 'aves.html')


def invertebrados(request) :
    return render(request, 'invertebrados.html')


def mamiferos(request) :
    return render(request, 'mamiferos.html')


def peixes(request) :
    return render(request, 'peixes.html')


def repteis(request) :
    return render(request, 'repteis.html')


def jogo(request) :
    contexto = {'perguntas' : Pergunta.objects.all(), 'pontuacao' :Resposta.objects.all()}
    Quizzz = Quizz.objects.all()
    pontos = 0
    ponto_1 = 0
    ponto_2 = 0
    ponto_3 = 0
    ponto_4 = 0
    ponto_5 = 0
    ponto_6 = 0
    ponto_7 = 0
    ponto_8 = 0
    ponto_9 = 0
    ponto_10 = 0
    if request.method == 'POST':
        resposta1 = request.POST.get('1')
        resposta2 = request.POST.get('2')
        resposta3 = request.POST.get('3')
        resposta4 = request.POST.get('4')
        resposta5 = request.POST.get('5')
        resposta6 = request.POST.get('6')
        resposta7 = request.POST.get('7')
        resposta8 = request.POST.get('8')
        resposta9 = request.POST.get('9')
        resposta10 = request.POST.get('10')
        resposta1 = resposta1.lower()
        resposta2 = resposta2.lower()
        resposta3 = resposta3.lower()
        resposta4 = resposta4.lower()
        resposta5 = resposta5.lower()
        resposta6 = resposta6.lower()
        resposta7 = resposta7.lower()
        resposta8 = resposta8.lower()
        resposta9 = resposta9.lower()
        resposta10 = resposta10.lower()
        if resposta1 == "áfrica":
            pontos = 2
            ponto_1 = 2
        if resposta2 == "mamifero":
            pontos = pontos + 2
            ponto_2 = 2
        if resposta3 == "seis":
            pontos = pontos + 2
            ponto_3 = 2
        if resposta4 == "5416":
            pontos = pontos + 2
            ponto_4 = 2
        if resposta5 == "verdadeiro":
            pontos = pontos + 2
            ponto_5 = 2
        if resposta6 == "1988":
            pontos = pontos + 2
            ponto_6 = 2
        if resposta7 == "chita":
            pontos = pontos + 2
            ponto_7 = 2
        if resposta8 == "baleia-azul":
            pontos = pontos + 2
            ponto_8 = 2
        if resposta9 == "formiga":
            pontos = pontos + 2
            ponto_9 = 2
        if resposta10 == "tatu":
            pontos = pontos + 2
            ponto_10 = 2
        Quizzz.update(pontuaçao=pontos)
        Nota.objects.all().delete()
        n = Nota.objects.create(quizz_id=Quizz.objects.get(pk=1), pontos=pontos)
        n.save()
        Resposta.objects.all().delete()
        l = Resposta.objects.create(respostas=resposta1, pontos=ponto_1)
        l.save()
        l = Resposta.objects.create(respostas=resposta2, pontos=ponto_2)
        l.save()
        l = Resposta.objects.create(respostas=resposta3, pontos=ponto_3)
        l.save()
        l = Resposta.objects.create(respostas=resposta4,pontos=ponto_4)
        l.save()
        l = Resposta.objects.create(respostas=resposta5, pontos=ponto_5)
        l.save()
        l = Resposta.objects.create(respostas=resposta6, pontos=ponto_6)
        l.save()
        l = Resposta.objects.create(respostas=resposta7, pontos=ponto_7)
        l.save()
        l = Resposta.objects.create(respostas=resposta8, pontos=ponto_8)
        l.save()
        l = Resposta.objects.create(respostas=resposta9, pontos=ponto_9)
        l.save()
        l = Resposta.objects.create(respostas=resposta10, pontos=ponto_10)
        l.save()
        return redirect('website:pontuacao')
    return render(request, 'jogo.html', contexto)


def about(request) :
    return render(request, 'sobre.html')


def pokedex(request) :
    return render(request, 'pokedex.html')


def login(request) :
    return render(request, 'login.html')


def comentario(request) :
    questionario = ComentarioForm(request.POST or None)
    if questionario.is_valid():
        data = questionario.cleaned_data
        P_clareza = data['clareza']
        P_originalidade = data['originalidade']
        P_design = data['design']
        P_rigor = data['rigor']
        print(P_rigor)
        questionario.save()
        field_name_Ex = 'Excelente'
        obj_1 = Comentario_values.objects.first()
        field_value = getattr(obj_1, field_name_Ex)

        field_name_Mb = 'Muito_Bom'
        obj_2 = Comentario_values.objects.first()
        field_value_1 = getattr(obj_2, field_name_Mb)

        field_name_B = 'Bom'
        obj_3 = Comentario_values.objects.first()
        field_value_2 = getattr(obj_3, field_name_B)

        field_name_M = 'Mau'
        obj_4 = Comentario_values.objects.first()
        field_value_3 = getattr(obj_4, field_name_M)

        field_name_P = 'Pessimo'
        obj_5 = Comentario_values.objects.first()
        field_value_4 = getattr(obj_5, field_name_P)

        if P_clareza == 'EXCELENTE':
            field_value += 1
        elif P_clareza == 'MUITO BOM':
            field_value_1 += 1
        elif P_clareza == 'BOM':
            field_value_2 += 1
        elif P_clareza == 'MAU':
            field_value_3 += 1
        else:
            field_value_4 += 1

        if P_originalidade == 'EXCELENTE' :
            field_value += 1
        elif P_originalidade == 'MUITO BOM':
            field_value_1 += 1
        elif P_originalidade == 'BOM':
            field_value_2 += 1
        elif P_originalidade == 'MAU':
            field_value_3 += 1
        else:
            field_value_4 += 1

        if P_design == 'EXCELENTE' :
            field_value += 1
        elif P_design == 'MUITO BOM':
            field_value_1 += 1
        elif P_design == 'BOM':
            field_value_2 += 1
        elif P_design == 'MAU':
            field_value_3 += 1
        else:
            field_value_4 += 1

        if P_rigor == 'EXCELENTE' :
            field_value += 1
        elif P_rigor == 'MUITO BOM':
            field_value_1 += 1
        elif P_rigor == 'BOM':
            field_value_2 += 1
        elif P_rigor == 'MAU':
            field_value_3 += 1
        else:
            field_value_4 += 1

        Comentario_values.objects.update(Excelente=field_value,Muito_Bom=field_value_1,Bom=field_value_2,Mau=field_value_3,Pessimo=field_value_4)
        return HttpResponseRedirect('grafico.html')
    contexto = {'form' : questionario ,
                'comentario_value' : Comentario_values.objects.all(),
                'comentario' : Comentario.objects.all()
                }
    return render(request, 'comentario.html', contexto)


def contato(request) :
    if request.user.is_authenticated :
        form = ContatoForm(request.POST or None)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('website:contatos'))
        context = {'form_contatos' : form, 'contatos' : Contato.objects.all()}
        return render(request, 'contato.html', context)
    return render(request, 'login.html')


def editar_contatos_view(request,contato_id):
    value = Contato.objects.get(id=contato_id)
    form = ContatoForm(request.POST or None, instance=value)
    print(form)
    if form.is_valid():
        print("1")
        form.save()
        return HttpResponseRedirect(reverse('website:contatos'))
    else:
        print("2")
    context = {'form_contatos' : form, 'contato_id' : contato_id}
    return render(request, 'editarcontatos.html', context)


def apaga_contato_view(request, contato_id):
    Contato.objects.get(id=contato_id).delete()
    return HttpResponseRedirect(reverse('website:index'))







def home_page_view1(request) :
    contexto = {'quizz' : Quizz.objects.all()}
    return render(request, './jogo.html', contexto)


def home_page_view2(request) :
    contexto = {'pergunta' : Pergunta.objects.all()}
    return render(request, './jogo.html', contexto)


def home_page_view3(request) :
    contexto = {'nota' : Nota.objects.all()}
    return render(request, './jogo.html', contexto)


class PersonListView(ListView) :
    model = Pokedex
    template_name = './pokedex.html'


def entrar_view(request) :
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None :
            auth_login(request, user)
            return render(request, "index.html", {
                'message' : 'Bem vindo.'
            })
        else :
            return render(request, "index.html", {
                'message' : 'Invalid credentials.'
            })
    return render(request, "login.html", {
        'message' : 'Insira as suas credenciais.'}
                  )


def logout_view(request) :
    logout(request)
    Contato.objects.all().delete()

    return render(request, 'index.html', {
        "message" : "Logout"
    })


def signup(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login.html')
    else :
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})


def pontuacao(request):

    contexto = {'perguntas': Pergunta.objects.all(),
                'respostas': Resposta.objects.all(),
                'notas': Nota.objects.all()}
    return render(request, 'pontuacao.html',contexto)


def grafico(request):
    mycolors = ["black", "hotpink", "b", "#4CAF50", "brown"]
    field_name_Ex = 'Excelente'
    obj_1 = Comentario_values.objects.first()
    field_value = getattr(obj_1, field_name_Ex)

    field_name_Mb = 'Muito_Bom'
    obj_2 = Comentario_values.objects.first()
    field_value_1 = getattr(obj_2, field_name_Mb)

    field_name_B = 'Bom'
    obj_3 = Comentario_values.objects.first()
    field_value_2 = getattr(obj_3, field_name_B)

    field_name_M = 'Mau'
    obj_4 = Comentario_values.objects.first()
    field_value_3 = getattr(obj_4, field_name_M)

    field_name_P = 'Pessimo'
    obj_5 = Comentario_values.objects.first()
    field_value_4 = getattr(obj_5, field_name_P)

    lista = []
    lista_chaves = ["Excelente", "Muito Bom", "Bom", "Mau", "Pessimo"]
    lista.append(field_value)
    lista.append(field_value_1)
    lista.append(field_value_2)
    lista.append(field_value_3)
    lista.append(field_value_4)
    plt.bar(lista_chaves, lista)
    plt.title("Quantidades de extensoes")
    plt.savefig('barchart.png')
    return render(request, 'grafico.html')



def java(request):
    return render(request,"javascript.html")
