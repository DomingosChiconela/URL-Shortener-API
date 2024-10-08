
import random
import string



def generate_short_url(length=6):
    
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    return f'https://shortener-0s3u.onrender.com/api/urls/{random_suffix}'