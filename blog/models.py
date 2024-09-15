from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')

    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    field_1 = models.IntegerField(default=0)
    field_2 = models.CharField(null = True)
    excerpt = models.CharField(null = True)
    
    def __str__(self):
        return f"The title of the post is {self.title}"

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
            return f"{self.title}| written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
            return f"Comment {self.body}| written by {self.author}"

    challenge = models.FloatField(default=3.0)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

def profile_page(request):
    user = get_object_or_404(User, user=request.user)
    # Retrieve all comments for the user object
    comments = user.commenter.all()