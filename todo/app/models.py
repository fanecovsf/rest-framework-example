from django.db import models

class Todo(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    def __str__(self) -> str:
        return self.desc

    desc = models.CharField(max_length=255)
    todo = models.ForeignKey(Todo, related_name='items', on_delete=models.PROTECT)

