from archus.mail import SendMail
from archus.status import HTTPStatus
from archus.response import Response


def index(request):
	return Response(HTTPStatus.OK, { "message": "Archus is up & running" })

def testMail(request):
	html_content = """
    <html>
        <body>
            <h1 style="color:blue;">Thank You for Choosing Us</h1>
            <p>This is the first mail from <strong>Archus</strong></p>
        </body>
    </html>
    """
	mail = SendMail()
	mail.send_email(
			subject="Archus - Testing Mail Service",
			to="supratimm531@gmail.com",
			body=html_content,
			html=True
	)
	return Response(HTTPStatus.OK, { "message": "POST request successful" })
