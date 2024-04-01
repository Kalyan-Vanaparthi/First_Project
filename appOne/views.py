from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f1(Request):
    return HttpResponse("This is Kalyan Vanaparthi😎")

def f2(Request):
    return HttpResponse('''<ol>
    <li>pookulo lo modda</li>
    <li> kuthalo modda</li>



                        </ol>
<a href="https://www.qorno.com/" target="_blank"> nokku ikkada </a>
<img src="https://res.cloudinary.com/dzeobljtb/image/upload/v1692452721/IMG_20230708_075058_fsbiwo.jpg" />
                        ''')