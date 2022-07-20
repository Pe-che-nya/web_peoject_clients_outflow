from django.shortcuts import render
navigation = [{
    'title': 'Информация',
    'link': '#'
},{
    'title': 'Учетка пользователя',
    'link': '#'
}]
def main(request):
    context = {'navigation': navigation}
    return render(request, 'listClients.html', context=context)
# Create your views here.
