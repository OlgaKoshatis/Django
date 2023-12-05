import logging

from django.http import HttpResponse

logger: logger = logging.getLogger(__name__)


def index(request):
    home_page = """<!DOCTYPE html>
    <html lang='en'>
        <head>
            <title>home_page</title>
        </head>
        <body>
            <h1>Здесь будет название приложения</h1>
            <p>It is a main page of my first site/application on <u>Django</u></p>
            <p><i>Here I'll write some information<br>about an application<br>but little later</i></p>
        </body>
    </html>"""
    logger.info('home page accessed')
    return HttpResponse(home_page)


def about(request):
    about_me = """<!DOCTYPE html>
    <html lang='en'>
        <head>
            <title>home_page</title>
            info about page structure
        </head>
        <body>
            <h1>Здесь будет что-то обо мне</h1>
            <p>and some more content<br>and more<br>that's it</p>
        </body>
    </html>"""
    logger.info('about page visited')
    return HttpResponse(about_me)

