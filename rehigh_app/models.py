from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField()
    content = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True) #date when created
    UpdatedAt = models.DateTimeField(auto_now=True)  #date when updated

    def __str__(self):
        return self.title


class Swiper(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField(blank=True, null=True)
        desktop_image = models.ImageField(blank=True, null=True)  # Image for the slide
        phone_image = models.ImageField(blank=True, null=True) #Image for phone mobiles
        button_text = models.CharField(max_length=50, blank=True, null=True)
        button_link = models.URLField(blank=True, null=True)

        def __str__(self):
            return self.title


class Variation(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200,blank=True,null=True)
    swiper = models.ForeignKey(Swiper, on_delete=models.CASCADE, related_name='variations')

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200, default='Unknown')
    phone_num = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.name











