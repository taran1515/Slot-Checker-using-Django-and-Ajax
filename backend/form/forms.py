from django import forms
from .models import TrialClass,Slots,TimeSlots

class TrialClassForm(forms.ModelForm):
    class Meta:
        model = TrialClass
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = Slots.objects.none()


        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                print(course_id)
                self.fields['slot'].queryset = Slots.objects.filter(course_id=course_id).order_by('slot_date')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['slot'].queryset = self.instance.course.slot_set.order_by('slot_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_slot'].queryset = TimeSlots.objects.none()


        if 'slot' in self.data:
            try:
                slot_id = int(self.data.get('slot'))
                print(slot_id)
                self.fields['time_slot'].queryset = TimeSlots.objects.filter(slot_id=slot_id).order_by('time_slot')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['time_slot'].queryset = self.instance.slot.time_slot_set.order_by('time_slot')

        
