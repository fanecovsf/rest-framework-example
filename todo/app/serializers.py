from app.models import Todo, Item

from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'desc',
            'todo'
        ]


class TodoSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = [
            'id',
            'name',
            'done',
            'created_at',
            'items'
        ]
