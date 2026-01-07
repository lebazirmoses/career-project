from django.shortcuts import render
from .models import CareerRecommendation

def sample_ai_view(request):
    # For demo purposes, static data
    recommendations = [
        {"career_name": "Data Scientist", "score": 85, "reason": "Strong math & AI skills"},
        {"career_name": "AI Engineer", "score": 78, "reason": "Good programming & ML knowledge"},
        {"career_name": "Software Developer", "score": 65, "reason": "Average AI exposure"},
    ]
    return render(request, "ai_career/recommendations.html", {"recommendations": recommendations})
