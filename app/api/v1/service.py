from archus.status import HTTPStatus
from archus.response import Response


def index(request):
	return Response(HTTPStatus.OK, { "message": "Archus is up & running" })