from django.template.defaultfilters import title

from blog.models import Message

from django import forms
from django.core.validators import ValidationError


# class ContactUsForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=50 , required=False)
#     text = forms.CharField(max_length=100, label='Your Message')
#     date = forms.DateField(label='Date' , widget = forms.SelectDateWidget)
#
#
# # dar form ag bkhahi, k bein field haye motfavet moqayese ii anjam bedim baid to method clean onaro modriat konim v havasemon b in bashe k tebq ketabkhone import shde dar bala khata haro raise konim v hmchnin khata haye in qesmat dar non filed errors namayesh dade mishan
#     def clean(self):
#         name = self.cleaned_data.get('name')
#         text = self.cleaned_data.get('text')
#         if name == text :
#             raise ValidationError('your name and text are same' , code='name_text_same')
#
#
#
#     # ag bkhahim k braye y fild khas shart gozari konim hatmn k baid mesl zir ono benevism v error haye ono modriat konim v neveshtan clean_esmfiled hatmn vajebe v inke in error to qesmat error haye khode on fild namayesh dade mishe v olaviat bala tri nesbat b error haye clean dare
#     # havasemon bashe k in tabe hatmn dar nahayt baid y return dashte bashe b in onvan k meqdar on sahihe v  az hame shart ha b drsty obor krde
#     # paiin mesal braye modriat name avarde shde v faqat brayesh neshon dadn modriat filed name mibashad
#
#     # def clean_name(self):
#     #     name = self.cleaned_data.get('name')
#     #     if 'a' in name:
#     #         raise ValidationError('your name is wrong' , code='name_a')
#     #     return name

# y ravesh sakhtm form b sorat dasty az ravesh bala bod vli raveshi k kheili bhine ast mannd zir ast k ma miaim bar asas model khodete jango form marbot b ono bramon misazw
class MassageForm(forms.ModelForm):
    class Meta:
      model = Message
      fields = '__all__'

    #
    # def clean_name(self):
    #   name = self.cleaned_data.get('name')
    #   if 'a' in name :
    #     print("lkkerg")
    #   return name
    #
    #     {# in khat b in manzore k ma baid braye hame field haye modelemon y input baiud baraye on dar nazar bgirim#} ag all bznim yani braye hame injad konm ama ge b sorat tuple ono benvisim faqat braye field haye tuple miad v input misaze
    #
    #
    #     exclude = ['user'] ==>> in bra zamanie k ma mikhaim hme braye hme feild ha input dashte bashim b joz inaii k dar in qesmat minevisim
    #
    #     zamani k ma miaim az in model class bandi ba tavajog b hme field ha automatic mikonim ono az in ravesh zir mitonim k b field haye khodmon widget bedim b ono shakhsi sazi konim
    #     tnha nokte iii k dare esm bakhsh haye mokhtakef daron dic widgets baid mesl model ma bashe
    #     zir y mesal braye zibatr kardn input haye name v title avorde shde
      widgets = {
          "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name : '}),
          "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Title : '}),
      }`