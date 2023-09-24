from django.db import models

class Todo(models.Model):
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateTimeField("締切", blank=True, null=True, default=None)

    def __str__(self):
        return self.title