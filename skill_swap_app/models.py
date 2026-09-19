from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserSkill(models.Model):
    
    SKILL_LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    SKILL_TYPES = [
        ('offer', 'Offer'),
        ('learn', 'Learn'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skill=models.ForeignKey(Skill,on_delete=models.CASCADE)
    skill_level=models.CharField(max_length=20,choices=SKILL_LEVELS)
    type=models.CharField(max_length=10,choices=SKILL_TYPES)

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"