from django.views.generic import CreateView

from contact.tasks import send_confirm_subscription_task
from .forms import ContactForm
from .models import Contact


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        send_confirm_subscription_task.delay(form.instance.email)
        return super().form_valid(form)
