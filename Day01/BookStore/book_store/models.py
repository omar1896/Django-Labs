from django.db import models
from django.core.validators import MinValueValidator

class Users(models.Model):
     name=models.CharField("name",max_length=50)
     phone=models.CharField("phone",max_length=15)

     
class ISBN(models.Model):
     isbn=models.BigAutoField(primary_key=True)    
     author_title=models.CharField(max_length=50)
     book_title=models.CharField(max_length=50,validators=[MinValueValidator(10)])


class Books(models.Model):
    ISBN = models.OneToOneField(
        ISBN,
        on_delete=models.CASCADE,
       
    )
    slug=models.SlugField(default="")
    title=models.CharField("title",max_length=50)
    views=models.IntegerField()
    rate=models.IntegerField()
    description=models.TextField('description')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)



    

class Category(models.Model):
      Name_of_Categories = [
        ("hrr", "Horror"),
        ("cd", "Comedy"),
        ("dra", "Drama"),
        ("sci", "Science"),
        ("hs", "History"),
    ]
      name=models.CharField( choices=Name_of_Categories,max_length=20,validators=[MinValueValidator(2)])
      book = models.ForeignKey(Books, on_delete=models.CASCADE)




