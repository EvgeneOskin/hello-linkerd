from logging import getLogger
import muffin
from aiohttp import web


logger = getLogger(__name__)


def mix_linkerd_tracer_headers(response, request, prefix):
    headers = {k: v for k, v in request.headers.items()
               if k.lower().startswith(prefix)}
    for k, v in headers.items():
        response.headers[k] = v
    logger.info(response.headers)


async def linkerd_tracer_middleware(app, handler):
    linker_prefix = app.cfg.LINKERD_TRACER_HEADER_PREFIX
    async def middleware_handler(request):
        try:
            response_headers = request.headers
            response = await handler(request)
            mix_linkerd_tracer_headers(response, request, linker_prefix)
            return response
        except web.HTTPException as ex:
            mix_linkerd_tracer_headers(ex, request, linker_prefix)
            raise
    return middleware_handler


app = muffin.Application(
    'app', middlewares=(linkerd_tracer_middleware,)
)


@app.register('/', '/hello/{name}')
def hello(request):
    name = request.match_info.get('name', 'World')
    return 'Hello, %s!' % (name,)
