from rest_framework import serializers
from .models import MONTHS, Podopieczny, Stanowisko
from rest_framework.validators import UniqueTogetherValidator
# class BookSerializer (serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)

#     title = serializers.CharField(required = True)

#     publication_month = serializers.ChoiceField(choices = MONTHS.choices, default = MONTHS.choices[0][0])

#     book_format = serializers.ChoiceField(choices = BOOK_FORMATS, default = BOOK_FORMATS[0][0])

#     author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all(), allow_null = True)

#     genere = serializers.PrimaryKeyRelatedField(queryset = Genre.objects.all(), allow_null = True)

#     available_copies = serializers.IntegerField(default = 1)

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.publication_month = validated_data.get('publication_month', instance.publication_month)
#         instance.book_format = validated_data.get('book_format', instance.book_format)
#         instance.author = validated_data.get('author', instance.author)
#         instance.genere = validated_data.get('genere', instance.genere)
#         instance.available_copies = validated_data.get('available_copies', instance.available_copies)
#         instance.save()
#         return instance
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
        validators = [
            UniqueTogetherValidator(
                queryset=Author.objects.all(),
                fields=['first_name', 'last_name']
            )
        ]

    def validate(self, data):
        """
        Walidacja całego obiektu autora.
        Sprawdza poprawność formatu imienia, nazwiska i kodu kraju.
        """
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        country = data.get('country')

        # Imię i nazwisko powinny zaczynać się wielką literą
        if first_name and not first_name.istitle():
            raise serializers.ValidationError(
                {"first_name": "Imię powinno rozpoczynać się wielką literą!"}
            )

        if last_name and not last_name.istitle():
            raise serializers.ValidationError(
                {"last_name": "Nazwisko powinno rozpoczynać się wielką literą!"}
            )

        # Kod kraju: dokładnie 2 wielkie litery
        if country and (len(country) != 2 or not country.isupper()):
            raise serializers.ValidationError(
                {"country": "Kod kraju musi składać się z 2 wielkich liter, np. 'PL'."}
            )

        return data
    
def multiple_of_two(value):
    if value % 2 != 0:
        raise serializers.ValidationError("Ocena popularności musi być wielokrotnością 2 (np. 0, 2, 4, 6, 8, 10).")
    
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
    
class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = "__all__"