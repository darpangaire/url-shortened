from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_code', 'created_at', 'click_count']
        read_only_fields = ['short_code', 'created_at', 'click_count']

    def create(self, validated_data):
        # You can plug in your custom short code generation logic here
        validated_data['short_code'] = self.generate_short_code()
        return super().create(validated_data)

    def generate_short_code(self):
        import string, random
        from .models import ShortenedURL

        length = 6
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(chars, k=length))
            if not ShortenedURL.objects.filter(short_code=code).exists():
                return code

