from django.db.models import CharField,IntegerField,Model,BinaryField,DateField

# Create your models here.
# class User(Model):
#     username=CharField(max_length=100)
#     password=CharField(max_length=100)
#     email=CharField(max_length=100)
#     phone=CharField(max_length=100)
#     profile_pic=BinaryField()

username="admin"
password="admin"
email="admin@gmail.com"
phone="2223334445"
profile_pic=None

class blog_table(Model):
    blog_title=CharField(max_length=100)
    blog_html=CharField(max_length=100) # denotes path to the html file of the blog
    date=DateField()
    media_id=CharField(max_length=100) # path to the media used

class media_table(Model):
    id_cus=IntegerField()
    data=BinaryField() # data => music,video,image

