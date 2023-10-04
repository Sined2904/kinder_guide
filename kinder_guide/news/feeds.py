from django.contrib.syndication.views import Feed  
from django.template.defaultfilters import truncatewords  
from .models import News  
  
  
class LatestNewsFeed(Feed):  
    title = 'Kinder guide latest news'
    link = '/news/'
    description = 'Updates on changes and additions to Kinder guide.'

    def items(self):
        return News.objects.order_by('-date_posted')[:3]
      
    def item_title(self, item):  
        return item.title  
      
    def item_description(self, item):  
        return truncatewords(item.content, 30)