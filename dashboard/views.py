from django.shortcuts import render, get_object_or_404
from .forms import LivestockForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Livestock

def dashboard(request):
    template = 'dashboard.html'
    return render(request, template, { })

def livestock_list(request):
    template = 'livestock_list.html'
    livestocks = Livestock.objects.all()
    return render(request, template, { })

# def base(request):
#     form = BookForm()
#     template = 'base.html'
#     context = {'form': form}
#     html_form = render_to_string('main/partial_book_create.html', context, request=request,)
#     return render(request, template, {})

def save_livestock_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        # form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            livestocks = Livestock.objects.all()
            data['html_livestock_list'] = render_to_string('new_livestock_list.html', {'livestocks': livestocks})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def livestock_create(request):
    if request.method == 'POST':
        form = LivestockForm(request.POST)
    else:
        form = LivestockForm()
    return save_livestock_form(request, form, 'livestock_create.html')

# def livestock_update(request, pk):
#     livestock = get_object_or_404(Livestock, pk=pk)
#     if request.method == 'POST':
#         form = LivestockForm(request.POST, instance=livestock)
#     else:
#         form = LivestockForm(instance=livestock)
#     return save_book_form(request, form, 'livestock_update.html')

# def livestock_delete(request, pk):
#     livestock = get_object_or_404(Livestock, pk=pk)
#     data = dict()
#     if request.method == 'POST':
#         livestock.delete()
#         data['form_is_valid'] = True
#         livestocks = Livestock.objects.all()
#         data['html_livestock_list'] = render_to_string('livestock_list.html', {'livestocks':livestocks})
#     else:
#         context = {'livestock': livestock}
#         data['html_form'] = render_to_string('livestock_delete.html', context, request=request,)
#     return JsonResponse(data)
    



