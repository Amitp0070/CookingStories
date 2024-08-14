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
    rating = models.FloatField(default=0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Number of ratings
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    likes = models.PositiveIntegerField("Total likes", default=0)
    author_image = models.ImageField("Author image", upload_to='authors/',)  # New field for author's image
    def update_rating(self, new_rating):
        total_rating = self.rating * self.rating_count
        self.rating_count += 1
        total_rating += new_rating
        self.rating = total_rating / self.rating_count
        self.save()
    def __str__(self):
        return self.title
    


    

    


