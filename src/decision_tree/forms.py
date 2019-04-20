from django import forms
from .models import Symptoms


class SymptomsForm(forms.ModelForm):

	class Meta:
		model = Symptoms
		fields = ["Fever", "Bilsters_in_the_mouth_and_on_feet", "Drop_in_milk_production", "Weight_loss", "Loss_of_appetite",
                  "blisters_on_teats", "Lameness", "intermittent_fever", "anaemia", "oedema", "lacrimation", "Lymph_nodes",
                  "Abortion", "Infertility", "emaciation", "Calf_dropping_the_head", "Dull_and_depressed",
                  "High_temperature", "Heavy_breathing", "Nasal_discharge", "Coughing", "Stillbirth", "Weak_calf_born",
                  "Retention_of_fetal_membranes", "infection_in_the_membranes", "Swollen_testicles_in_bulls", "Watery_Milk",
                  "heat", "Swollen_udder", "Pain_in_udder", "Hardness_of_the_teats", "reduction_in_milk", "anorexia",
                  "corneal_opacity", "diarrhoea", "milky_eye_and_white_gums"]
