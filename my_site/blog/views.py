from django.views.generic.base import TemplateView


class Information(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(Information, self).get_context_data(**kwargs)
        return context
