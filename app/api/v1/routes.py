from .service import index, testMail


v1_urls = [
	{ 'path': '/', 'method': ['GET'], 'handler': index },
	{ 'path': '/testMail', 'method': ['POST'], 'handler': testMail },
]