from django.db import models

class Wood(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    color = models.CharField(max_length=100)
    grain = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    durability = models.CharField(max_length=100)
    uses = models.TextField()
    care_instructions = models.TextField()
    image1 = models.ImageField(upload_to='woods/', blank=True, null=True)
    image2 = models.ImageField(upload_to='woods/', blank=True, null=True)
    image3 = models.ImageField(upload_to='woods/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/woods/{self.id}/'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='woods/', blank=True, null=True)


    def __str__(self):
        return self.name