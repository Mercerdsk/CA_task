from django.shortcuts import render, redirect
from .forms import NotifyForm
from .models import Notify

def gridview(request):
    if request.method == 'POST':
        form = NotifyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gridview')
    else:
        form = NotifyForm()

    people = Notify.objects.all()
    context = {'form': form, 'people': people}
    return render(request, 'gridview.html', context)
