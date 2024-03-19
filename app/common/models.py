from django.db import models

class CommonModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True) # 생성된 시간 (시간 고정)
    updated_at = models.DateTimeField(auto_now=True) # 데이터가 업데이터 된 시간 (업데이트 할 때 마다 계속 시간이 변경)

    class Meta:
        abstract = True # DB에 테이블을 추가하지 마시오.