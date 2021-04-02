from .models import Post
from django.utils import timezone


def get_popular_posts(request):
	
    return {
        'popular_posts': Post.objects.filter(date_posted__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
                                             ).order_by('-post_views')[:5]}
