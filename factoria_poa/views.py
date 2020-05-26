from django.shortcuts import render, redirect


def pagina_principal(request):
    context = {'titulo': 'Página principal'}
    return render(request, 'principal.html', context)