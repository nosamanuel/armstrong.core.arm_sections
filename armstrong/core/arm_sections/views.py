from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from .models import Section


class SimpleSectionView(TemplateView):
    well_title = None

    def get_section(self):
        return Section.objects.get(full_slug=self.kwargs['full_slug'])

    def get_context_data(self, **kwargs):
        context = super(SimpleSectionView, self).get_context_data(**kwargs)
        context["section"] = self.get_section()
        return context
