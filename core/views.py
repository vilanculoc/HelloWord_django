from django.shortcuts import render, HttpResponse

# Create your views here.
#def hello(request, nome):
   # return HttpResponse('<h1>Hello {}<h1>'.format(nome))

def hello(request, valor1, valor2):
    a=int(valor1)
    b=int(valor2)
    soma=a+b
    subtracao=a-b
    mult=a*b
    divisao=a/b
    return HttpResponse('<h1> Ola Celsa Vilanculo.</h1><p> voce digitou: '
                        '<br> o primeiro valor = {} '
                        '<br> o segundo valor = {}.'
                        '<br> A soma = {}'
                        '<br> A Subtracao = {}'
                        '<br> A Multiplicacao = {}'
                        '<br> A Divisao = {}</p>'.format(a, b, soma, subtracao, mult, divisao))
