from .models import Post, Category

a = Post.objects.count()
print(a)

b = Category.objects.count()
print(b)
