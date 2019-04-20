import csv
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SymptomsForm
from .D_tree import predict


class ResultView(LoginRequiredMixin, TemplateView):
    template_name = 'decision_tree/result.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultView, self).get_context_data(*args, **kwargs)
        context['prediction'] = predict()
        return context


class SymptomView(LoginRequiredMixin, FormView):
    form_class = SymptomsForm
    template_name = 'decision_tree/diagnose.html'
    success_url = 'result'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        Values = []

        for field in form:
            if field.value():
                Values.append(1)
            else:
                Values.append(0)
        print(Values)

        writer = csv.writer(open("data.csv", "w+"))
        writer.writerow(["Fever", "Bilsters in the mouth and on feet", "Drop in milk production", "Weight loss", "Loss of appetite", "blisters on teats", "Lameness", "intermittent fever", "anaemia", "oedema", "lacrimation", "Lymph nodes", "Abortion", "Infertility", "emaciation", "Calf dropping the head", "Dull and depressed", "High temperature", "Heavy breathing", "Nasal discharge", "Coughing", "Stillbirth", "Weak calf born", "Retention of fetal membranes", "infection in the membranes", "Swollen testicles in bulls", "Watery Milk", "heat", "Swollen udder", "Pain in udder", "Hardness of the teats", "reduction in milk ", "anorexia", "corneal opacity", "diarrhoea", "milky eye and white gums"])
        writer.writerow(Values)

        return super(SymptomView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(SymptomView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Choose From The Clinical Symptoms and Then Submit'
        context['button'] = 'Submit'
        return context

'''
def write_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = "data.csv"'
    writer = csv.writer(response)
    writer.writerow(["fever", "loss_app", "red_eyes", "low_milk", "rot_foot", "rot_mouth"])
    writer.writerow()

    return response
'''