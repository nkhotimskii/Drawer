from rest_framework import serializers

from drawer import models


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Project
        fields = '__all__'


class PlanSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Plan
        fields = '__all__'


class ProjectWithPlansSerializer(serializers.ModelSerializer):

    plans = PlanSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ['name', 'details', 'plans']