from io import BytesIO
from PIL import Image
from core import HttpException, HttpResponse, startProfiling, stopProfiling
from core.http import HttpFile
import settings


def helloworld(request):
    if settings.PROFILING:
        prof = startProfiling()
    result = { "message": "Hello World" }
    if settings.PROFILING:
        stopProfiling(prof)
    return HttpResponse(result, 200)
