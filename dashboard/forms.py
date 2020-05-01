from django import forms 
from .models import Livestock

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock 
        fields = ('name', 'livestock_type', 'internal_id', 'key_words', 'status', 'breeding_stock',
                    'sex', 'breed', 'breed', 'coloring', 'retention_score', 'description', 
                    'tag_numbers', 'other_tag_numbers', 'birth_date', 'birth_weight', 'raised_purchased',
                    'veterinarian', 'on_feed', 'feed_type', 'feed_cost', 'measure_harvest', 'estimated_revenue' )


    