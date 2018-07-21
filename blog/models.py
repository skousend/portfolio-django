from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 75)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    
    def __str__(self):
        return self.title
    
    def summary(self):
        wordlist = self.body.split()
        return ' '.join(wordlist[:15]) + '...'
        
#    def pubdatepretty(self):
#           # see strftime.org for reference
#        return self.pub_date.strftime('%b %e %Y')
#   
