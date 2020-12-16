from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Contact'
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.email
    
    
