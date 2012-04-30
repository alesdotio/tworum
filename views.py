from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

class PostFormView(CreateView):

    def get_initial(self):
        initial = super(PostFormView, self).get_initial()
        initial = initial.copy()
        initial['thread'] = self.kwargs.get('pk')
        return initial

    def get_success_url(self):
        return reverse('thread_detail', args=[self.kwargs.get('pk')])