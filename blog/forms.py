from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    text = forms.CharField(max_length=100, label='Your Message')

# dar form ag bkhahi, k bein field haye motfavet moqayese ii anjam bedim baid to method clean onaro modriat konim v havasemon b in bashe k tebq ketabkhone import shde dar bala khata haro raise konim v hmchnin khata haye in qesmat dar non filed errors namayesh dade mishan
    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text :
            raise ValidationError('your name and text are same' , code='name_text_same')



    # ag bkhahim k braye y fild khas shart gozari konim hatmn k baid mesl zir ono benevism v error haye ono modriat konim v neveshtan clean_esmfiled hatmn vajebe v inke in error to qesmat error haye khode on fild namayesh dade mishe v olaviat bala tri nesbat b error haye clean dare
    # havasemon bashe k in tabe hatmn dar nahayt baid y return dashte bashe b in onvan k meqdar on sahihe v  az hame shart ha b drsty obor krde
    # paiin mesal braye modriat name avarde shde v faqat brayesh neshon dadn modriat filed name mibashad

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError('your name is wrong' , code='name_a')
    #     return name

