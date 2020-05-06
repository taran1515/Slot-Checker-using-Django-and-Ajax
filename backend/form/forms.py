from django import forms
from .models import TrialClass,Slots

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
                self.fields['slot'].queryset = Slots.objects.filter(course_id=course_id).order_by('slot_date')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['slot'].queryset = self.instance.course.slot_set.order_by('slot_date')