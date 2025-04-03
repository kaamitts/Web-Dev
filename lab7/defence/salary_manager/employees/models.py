from django.db import models
import json

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.JSONField(default=list)
    
    def  get_total_salary(self):
        total_bonus = sum(self.bonuses) if self.bonuses else 0
        return self.salary + total_bonus
    
    def get_highest_bonus(self):
        if not self.bonuses:
            return None
        return max(self.bonuses)
    
    def __str__(self):
        return self.name