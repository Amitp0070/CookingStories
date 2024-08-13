from django.db import models
from ckeditor.fields import RichTextField



class Topic(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField("Article title", max_length=100)
    image = models.ImageField("Article image", upload_to="articles/images",)
    content = RichTextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True,)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    likes = models.PositiveIntegerField("Total likes", default=0)
    author_image = models.ImageField(upload_to='authors/', blank=True, null=True)  # New field for author's image
    def __str__(self):
        return self.title
    

    


