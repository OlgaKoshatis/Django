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
            <h1>It is a main page of my first site/application on <u>Django</u></h1>
            <p><em>It is next point.<br>it has to be a multiline text to suit the others who checks
    our(students) homeworks</p>
        </body>
    </html>"""
    logger.info('home page accessed')
    return HttpResponse(home_page)


def about(request):
    about_me = """<!DOCTYPE html>
    <html lang='en'>
        <head>
            <title>home_page</title>
            Some info about page structure
        </head>
        <body>
            <h1>Заголовок</h1>
            <p>and some more content<br>and more<br>that's it</p>
        </body>
    </html>"""
    logger.info('about page visited')
    return HttpResponse(about_me)

