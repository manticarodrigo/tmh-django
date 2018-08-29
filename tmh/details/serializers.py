from rest_framework import serializers
from .models import ProjectDetail

class ProjectDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectDetail
        fields = '__all__'

    created_date = serializers.DateTimeField(read_only=True)
    type = serializers.ChoiceField(choices=ProjectDetail.TYPE_CHOICES)

    def get_image(self, obj):
        request = self.context.get('request')
        image = obj.image.url
        return request.build_absolute_uri(image)