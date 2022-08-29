from rest_framework import serializers

from blog.models import Men


class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men
        fields = ('title', 'time_create', 'is_published', 'category')