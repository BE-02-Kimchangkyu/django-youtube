from django.db import models
from common.models import CommonModel
from user.models import User

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() #S3 Bucket -> Save file -> URL -> SaveURL
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법

    user = models.ForeignKey(User, on_delete=models.CASCADE) # 운영의 문제. 유저가 없어지면 비디오도 없어진다.

# User: Video -> User: 다수의 비디오 -> YES
# Video: 비디오 하나에 다수의 유저 -> NO
# User:Video = 1:N