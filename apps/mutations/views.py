#
# Copyright (C) 2016   Dr. Maha Farhat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# pylint: disable=too-few-public-methods
#
"""
Provides the drug, locus, mutation data for the progressive dropdown inputs.
"""

from apps.maps.mixins import JsonView

from django.views.generic import TemplateView, FormView, DetailView, ListView
from django.core.urlresolvers import reverse

from .models import ImportSource, Drug, GeneLocus
from .forms import DataUploaderForm
from .utils import info_mutation_format

class MutationView(TemplateView):
    """View mutations"""
    template_name = "mutations/mutation.html"

    def get_context_data(self, **kw):
        """Gather together info of mutations"""
        dat = super(MutationView, self).get_context_data(**kw)
        if 'mutation' in self.request.GET:
            dat['highlight'], dat['regular_exp'], dat['info'] =\
                info_mutation_format(self.request.GET['mutation'])
        return dat


class UploadData(FormView):
    """Upload a new data importer."""
    title = "Upload Data to GenTB Mutations Tracker"
    template_name = 'mutations/upload_data.html'
    form_class = DataUploaderForm

    def get_success_url(self):
        """Return the Status page for the uploaded data"""
        return self.object.get_absolute_url()

    def form_valid(self, form):
        """The form isvalid so we'll save our form"""
        self.object = form.save(self.request.user) # pylint: disable=attribute-defined-outside-init
        return super(UploadData, self).form_valid(form)


class UploadView(DetailView):
    """A view of uploads"""
    template_name = 'mutations/upload_status.html'
    model = ImportSource


class UploadList(ListView):
    """A way to list a uploaded imports"""
    model = ImportSource
    title = "My Imports"
    parent = ("/maps/", "Maps")

    def get_queryset(self):
        """Return all import sources owned by the logged in user"""
        qset = super(UploadList, self).get_queryset()
        return qset.filter(uploader=self.request.user)


class DropDownData(JsonView):
    """Drop and drag data response"""
    def get_context_data(self, *args, **kwargs):
        """Gather together all the data for drugs"""
        super(DropDownData, self).get_context_data(*args, **kwargs)
        ret = {
            'levels': ['Drug', 'Gene Locus', 'Mutation'],
            'children': [],
        }
        for drug in Drug.objects.all():
            ret['children'].append({
                'name': str(drug),
                'children': [],
            })
            qset = drug.mutations.all()
            if not self.request.GET.get('all', False):
                qset = qset.filter(predictor=True)
            loci = qset.values_list('gene_locus__name', flat=True).distinct()
            for locus in GeneLocus.objects.filter(name__in=loci):
                ret['children'][-1]['children'].append({
                    'name': str(locus),
                    'children': [],
                })
                for mutation in qset.filter(gene_locus__name=locus):
                    ret['children'][-1]['children'][-1]['children'].append({
                        'name': str(mutation),
                        'value': mutation.name,
                    })
        return ret
