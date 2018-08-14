from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Transaction

class TransactionList(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction/list.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(
                user = self.request.user)

class TransactionCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transaction
    fields = ['type', 'date', 'category', 'member', 'tag', 'amount', 'description']
    template_name = 'transaction/form.html'
    success_url = reverse_lazy('transaction-add')
    success_message = "%(type)s - %(category)s was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransactionUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transaction
    fields = ['type', 'date', 'category', 'member', 'tag', 'amount', 'description']
    template_name = 'transaction/form.html'
    success_url = reverse_lazy('transaction-list')
    success_message = "%(type)s - %(category)s was updated successfully"

    def get_queryset(self):
        return super().get_queryset().filter(
                user=self.request.user)

class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction-list')
    success_message = "%(type)s  was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == request.user:
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        else:
            raise Http404