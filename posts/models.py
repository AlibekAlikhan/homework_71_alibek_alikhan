from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.CharField(verbose_name='Описание', null=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='posts')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    likes = models.IntegerField(verbose_name="Количество Лайков", default=0)
    comment = models.IntegerField(verbose_name="Количество Комментариев", default=0)

    def plus(self, using=None, keep_parents=False):
        self.likes += 1
        self.save()

    def minus(self, using=None, keep_parents=False):
        self.likes -= 1
        self.save()



class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False, blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='comments', null=False,
                             blank=False,
                             on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Комментарий', null=False, blank=False, max_length=200)


