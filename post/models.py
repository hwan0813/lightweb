import re
from django.db import models
from django.conf import settings
from django.forms import ValidationError
from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('invalid LngLat Type')

STATUS_CHOICES = (
    ('a', '일상 글'),
    ('b', '공지사항'),
    ('c', '라내방송'),
)

class Post(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    #아래처럼 하면 화살표눌러서 기사, 스포츠, 등등에서 선택하게 해줌.
    #title = models.CharField(max_length=100,
    #    choices = (
    #        ('제목1', '기사'), # ('저장된값','UI에 보여질레이블')
    #        ('제목2', '스포츠'),
    #        ('제목3', '등등'),
    #    ))
    #길이 제한이 있는 문자열 -> 캐릭터필드
    content = models.TextField(verbose_name="내용" , 
        help_text='여기에 내용을 입력하세요!') #verbose네임하면 필드입력이 이렇게 보여짐
        #help 텍스트하면 입력폼위에 회색글씨 작은걸로 도움말. 
    #길이 제한이 없는 문자열 -> 텍스트필드, 데이터베이스는 엄연히 다르니까.
    
    #이미지를 저장할수있는 필드 추가하고, 멬마그레이션+ 마이그레잇
    # upload_to 에 경로지정시 / 절대 쓰지말고 일단 걍써라. 그러며 ㄴ기존에 걍 media 아래저장되던게
    # media/dojo/post 밑으로저장됨
    # 저기에 또 /%Y/%m/%d 추가해주면 올린 년/달/일자 폴더로 구분되어서 업로드됨 ㅎㄷㄷ
    photo = ProcessedImageField(blank=True, upload_to='post/%Y/%m/%d',
                            processors=[Thumbnail(300,300)],
                            format="JPEG",
                            options={'quality': 60})
                                
    tag_set = models.ManyToManyField('Tag', blank = True)
    #그냥 Tag하면 안되는이유가 Tag클래스가 이거보다 뒤에 정의되어있기때문. 그래서 이렇게하는거. 

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tags = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True) # 날짜와 시간,. 오토나우애드 =>
    # 현재 하나의 포스트 레코드가 최초저장될때 일시가 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해동레코드가 갱신될때마다 일시가 자동 저장.

    class Meta: #기본 정렬 옵션 지정해주는것. id기준으로 역순 출력되도록. 
        ordering = ['-id']
        

    def __str__(self):
        return self.title

    #이걸 반드시 구현하라 . 그래야 코드의 효율성이 많이 올라감. 별 50개
    # 이렇게 하면 post = Post.objects.get(id=10)한다음 resolve_url(post)하면 바로 이게 /dojo/10/을 의미하게 됨. 
    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name