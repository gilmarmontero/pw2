from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, Movimento_Rotativo, Mensalista, Parametro_mensal, MovMensalista, Marca, Parametro_hora 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import PessoaForm, mensalForm, horaForm, VeiculoForm, Mov_RotativoForm, MensalistaForm, Mov_MensalistaForm, MarcaForm
from django.contrib.auth.decorators import login_required

def logar(request):
    return render(request, 'core/login.html',{})

def sair(request):
    logout(request)
    return render(request, 'core/login.html', {})

def login_views(request):  
    use = request.POST['usuario']
    senha = request.POST['senha']
    msg = False
    if request.method == "POST":
        user = authenticate(request, username=use, password=senha)
        if user is not None:
            login(request, user)
            return render(request, 'core/index.html', {'user': user}) 
        else:
            return render(request, 'core/login.html', {'msg':True}) 
    
    return render(request, 'core/login.html', {'msg':msg})
        

def home(request, pk):
    user = User.objects.get(pk = pk)
    return render(request, 'core/index.html', {'user':user})






def lista_pessoa(request, pk):
    pessoas = Pessoa.objects.all()
    user = User.objects.get(pk = pk)
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form, 'user': user}
    return render(request, 'core/lista_pessoa.html', data )


def pessoa_novo(request, pk):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    lista = "/pessoa/" + str(pk)   
    return redirect(lista)


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            upessoa = "/pessoa/" + request.POST['user'] 
            return redirect(upessoa)
    else:
        return render(request, 'core/update_pessoa.html', data)


    


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        upessoa = "/pessoa/" + request.POST['user'] 
        return redirect(upessoa)
    else:
        return render(request, 'core/delete_confirma.html', {'obj': pessoa})





def lista_veiculo(request, pk):
    veiculos = Veiculo.objects.all()
    user = User.objects.get(pk = pk)
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form, 'user': user}
    return render(request, 'core/lista_veiculo.html', data )


def veiculo_novo(request, pk):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    veiculo = "/veiculo/" + str(pk)   
    return redirect(veiculo)
    

def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            uveiculo = "/veiculo/" + request.POST['user'] 
            return redirect(uveiculo)
    else:
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        uveiculo = "/veiculo/" + request.POST['user'] 
        return redirect(uveiculo)
    else:
        return render(request, 'core/delete_confirma.html', {'obj': veiculo})




def lista_marca(request, pk):
    marca = Marca.objects.all()
    user = User.objects.get(pk = pk)
    form = MarcaForm()
    data = {'marca': marca, 'form': form, 'user': user}
    return render(request, 'core/lista_marca.html', data )

def marca_novo(request, pk):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    marca = "/marca/" + str(pk)   
    return redirect(marca)   
    


def marca_update(request, id):
    data = {}
    marca = Marca.objects.get(id=id)
    form = MarcaForm(request.POST or None, instance=marca)
    data['marca'] = marca
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            umarca = "/marca/" + request.POST['user'] 
            return redirect(umarca)
    else:
        return render(request, 'core/update_marca.html', data)









def lista_mov_rotativo(request, pk):
    mov_rotativo = Movimento_Rotativo.objects.all()
    user = User.objects.get(pk = pk)
    form = Mov_RotativoForm()
    data = {'mov_rotativo': mov_rotativo, 'form': form, 'user':user}
    return render(request, 'core/lista_mov_rotativo.html', data)


def rotativo_novo(request, pk):
    form = Mov_RotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    rotativo = "/movimento/" + str(pk)   
    return redirect(rotativo)   
    


def rotativo_update(request, id):
    data = {}
    movimento = Movimento_Rotativo.objects.get(id=id)
    form = Mov_RotativoForm(request.POST or None, instance=movimento)
    data['movimento'] = movimento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            umov = "/movimento/" + request.POST['user'] 
            return redirect(umov)
    else:
        return render(request, 'core/update_mov_rotativo.html', data)


def mov_rotativo_delete(request, id):
    mov = Movimento_Rotativo.objects.get(id=id)
    if request.method == 'POST':
        mov.delete()
        umov = "/movimento/" + request.POST['user'] 
        return redirect(umov)
    else:
        return render(request, 'core/delete_confirma.html', {'obj': mov})



        





def lista_mensalista(request, pk):
    mensalistas = Mensalista.objects.all()
    user = User.objects.get(pk = pk)
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form, 'user': user}
    return render(request, 'core/lista_mensalista.html', data)


def mensalista_novo(request, pk):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    mensal = "/mensalista/" + str(pk)   
    return redirect(mensal)   
    

def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            umensal = "/mensalista/" + request.POST['user'] 
            return redirect(umensal)
    else:
        return render(request, 'core/update_mensalista.html', data)


def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        umensal = "/mensalista/" + request.POST['user'] 
        return redirect(umensal)
    else:
        return render(request, 'core/delete_confirma.html', {'obj': mensalista})







def lista_mov_mensalista(request, pk):
    mov_mensal = MovMensalista.objects.all()
    user = User.objects.get(pk = pk)
    form = Mov_MensalistaForm() 
    data = {'mov_mensal': mov_mensal, 'form': form, 'user':user}
    return render(request, 'core/lista_mov_mensalista.html', data)

def mov_mensalista_novo(request):
    form = Mov_MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mov_mensalista')


def mov_mensalista_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = Mov_MensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mov_mensalista')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)   


def mov_mensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        mov_mensalista.delete()
        return redirect('mov_mensalista')
    else:
        return render(request, 'core/delete_confirma.html', {'obj': mov_mensalista}) 




def listaparametro_hora(request, pk):
    horas = Parametro_hora.objects.all()
    user = User.objects.get(pk = pk)
    form = horaForm()
    data = {'horas': horas, 'form': form, 'user': user}
    return render(request, 'core/lista_parametro_hora.html', data )


def parametrohora_novo(request, pk):
    form = horaForm(request.POST or None)
    if form.is_valid():
        form.save()
    lista = "/listaparametro_hora/" + str(pk)   
    return redirect(lista)


def parametrohora_update(request, id):
    data = {}
    parametro = Parametro_hora.objects.get(id=id)
    form = horaForm(request.POST or None, instance=parametro)
    data['parametro'] = parametro
    data['form'] = form
   

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            uparametro = "/listaparametro_hora/" + request.POST['user'] 
            return redirect(uparametro)
    else:
        return render(request, 'core/update_parametrohora.html', data)  

    
def parametrohora_delete(request, id):
    parametro = Parametro_hora.objects.get(id=id)
    if request.method == 'POST':
        parametro.delete()
        uparametro = "/listaparametro_hora/" + request.POST['user'] 
        return redirect(uparametro)
    else:
        return render(request, 'core/delete_confirma.html', {'obj': parametro})





def listaparametro_mensal(request, pk):
    p_mensal = Parametro_mensal.objects.all()
    user = User.objects.get(pk = pk)
    form = mensalForm()
    data = {'p_mensal': p_mensal, 'form': form, 'user': user}
    return render(request, 'core/lista_parametro_mensal.html', data )


def parametromensal_novo(request, pk):
    form = mensalForm(request.POST or None)
    if form.is_valid():
        form.save()
    lista = "/listaparametro_mensal/" + str(pk)   
    return redirect(lista)


def parametromensal_update(request, id):
    data = {}
    mensal = Parametro_mensal.objects.get(id=id)
    form = mensalForm(request.POST or None, instance=mensal)
    data['mensal'] = mensal
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            umensal = "/listaparametro_mensal/" + request.POST['user'] 
            return redirect(umensal)
    else:
        return render(request, 'core/update_parametromensal.html', data)


def parametromensal_delete(request, id):
    mensal = Parametro_mensal.objects.get(id=id)
    if request.method == 'POST':
        mensal.delete()
        umensal = "/listaparametro_mensal/" + request.POST['user']
        return redirect(umensal)
    else:
        return render(request, 'core/delete_confirma.html', {'obj': mensal}) 