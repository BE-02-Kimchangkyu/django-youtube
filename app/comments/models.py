from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저가 사라지면 댓글도 사라진다.
    # User : Comments = 1 : N // FK는 Comments

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # Video : Comments = 1 : N
