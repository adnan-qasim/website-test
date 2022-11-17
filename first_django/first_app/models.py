from django.db import models

# Create your models here.
class Accounts(models.Model):
    Full_name = models.CharField(max_length = 128)
    Username = models.CharField(max_length = 16,unique=True)
    e_Mail= models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    
    def __str__(self) -> str:
        return super().__str__()


class Articles(models.Model):
    Username = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    Article_id = models.IntegerField(unique = True)
    Article_Content = models.TextField()
    Date_Posted = models.DateTimeField(auto_now_add = True)
     
    def __str__(self) -> str:
        return super().__str__()


class Comments(models.Model):
    Article_id = models.ForeignKey(Articles,on_delete=models.CASCADE)
    Comment_id = models.IntegerField(unique = True)
    Comment_Username = models.CharField(max_length = 16,unique=True)
    Comment = models.TextField()

    def __str__(self) -> str:
        return super().__str__()

class Articles_Details(models.Model):
    Article_id = models.ForeignKey(Articles,on_delete=models.CASCADE,)
    Likes = models.IntegerField()
    Re_Posts = models.PositiveIntegerField()
    Post_Comments = models.ForeignKey(Comments,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()