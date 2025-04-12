from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()
    
    class Meta:
        db_table = 'Company'
    
    def __str__(self):
        return self.name    
    
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    
    class Meta:
        db_table = 'Vacancy'
    
    def __str__(self):
        return self.name   