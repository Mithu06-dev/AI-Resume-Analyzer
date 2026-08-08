from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    extracted_text = models.TextField(blank=True)

    ats_score = models.IntegerField(default=0)
    grammar_score = models.IntegerField(default=0)
    keyword_score = models.IntegerField(default=0)
    overall_score = models.IntegerField(default=0)

    suggestions = models.TextField(blank=True)

    def __str__(self):
        return self.file.name