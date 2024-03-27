from django.db import models
from common.models import CommonModel


# ChatRoom을 분리했을 때의 이점
# - 관리의 용이
# - 확장성 (채팅방: 오픈채팅방, 업무채팅방-비번입력)
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # SET_NULL - sender null 값으로 두겠다는 뜻. 1번 -> 계정삭제 -> null
    sender = models.ForeignKey("users.User",on_delete=models.SET_NULL, null=True) # 알 수 없음
    message = models.TextField()
    room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)

# User:Msg(FK) => 1:N 
    
# Room:Msg(FK) => 1:N