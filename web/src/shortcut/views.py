from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import View
from django.core.cache import cache

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
            shortcut = cache.get(web_addr)
            if not shortcut:
                short_url, _ = Url.objects.get_or_create(web_addr=web_addr)
                shortcut = short_url.shortcut
                cache.set(web_addr, shortcut, 30)
            return render(request, self.template_name, {'form':form, 'shortcut':shortcut})
        return render(request, self.template_name, {'form': form})

class GetShortcut(View):
    def get(self, request, code, *args, **kwargs):
        try:
            host_code, path_code = code.split('-')
        except:
            raise Http404("Short address isn't existed")
        addr = cache.get(code)
        if not addr:
            addr = get_object_or_404(Url, path_code=path_code, host_code__addr_code=host_code).web_addr
            cache.set(code, addr, 30)
        return redirect(addr)
