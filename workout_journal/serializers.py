from rest_framework import serializers
from .models import MONTHS, Podopieczny, Specjalizacja, Trener
from rest_framework.validators import UniqueTogetherValidator
class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trener
        fields = '__all__'
        
        validators = [
            UniqueTogetherValidator(
                queryset=Trener.objects.all(),
                fields=['imie', 'nazwisko']
            )
        ]

    def validate(self, data):
        first_name = data.get('imie')
        last_name = data.get('nazwisko')

        # Imię i nazwisko powinny zaczynać się wielką literą
        if first_name and not first_name.istitle():
            raise serializers.ValidationError(
                {"imie": "Imię powinno rozpoczynać się wielką literą!"}
            )

        if last_name and not last_name.istitle():
            raise serializers.ValidationError(
                {"nazwisko": "Nazwisko powinno rozpoczynać się wielką literą!"}
            )

        return data
    
class PodopiecznySerializer(serializers.ModelSerializer):
    class Meta:
        model = Podopieczny
        fields = "__all__"
        
    def validate_imie(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Imię powininno zawierać tylko litery i rozpoczynać się wielką literą!"
            )
        return value
    
    def validate_nazwisko(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Nazwisko powininno zawierać tylko litery i rozpoczynać się wielką literą!"
            )
        return value
    
class SpecjalizacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specjalizacja
        fields = "__all__"