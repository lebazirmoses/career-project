from django.db import models

class CareerRecommendation(models.Model):
    career_name = models.CharField(max_length=100)
    suitability_score = models.FloatField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.career_name} ({self.suitability_score}%)"
