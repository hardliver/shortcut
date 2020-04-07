from django.shortcuts import render
from django.views import View

from .forms import ShortcutForm
from .models import Url

class Shortcut(View):
    form_class = ShortcutForm
    template_name = 'shortcut.html'

    def get(self, request, *args, **kwargs):
        form = ShortcutForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ShortcutForm(request.POST)
        if form.is_valid():
            web_addr = request.POST.get('web_addr', '')
            short_url, _ = Url.objects.get_or_create(web_addr=web_addr)
            shortcut = short_url.shortcut
            return render(request, self.template_name, {'form':form, 'shortcut':shortcut})
        return render(request, self.template_name, {'form': form})
