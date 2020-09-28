from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


# # Roberth SoilsのDjango拡張機能が入っていると爆速でコーディングが進む
# # Model
# class Handson(models.Model):
#     # fk
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     # mchar
#     title = models.CharField(max_length=50)
#     # mtext
#     body = models.TextField()
#     # mdatetime
#     date = models.DateTimeField()
#     # mdatetime
#     created_at = models.DateTimeField(auto_now_add=True)
#     # mdatetime
#     updated_at = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Handson'
#         verbose_name_plural = 'Handsons'
