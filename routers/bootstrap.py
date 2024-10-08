from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.config.env import environment
from app.middlewares.authentication import BearerTokenTenantAuthBackend
from app.middlewares.exception import ExceptionHandlerMiddleware
from app.middlewares.profiler import register_profiler_middlewares
from app.routers import bulk_renderlink, core_auto_suggest, core_search
from app.routers import extras_kaas
from starlette.middleware.authentication import AuthenticationMiddleware

# Search Application
subapp = FastAPI(
    debug=environment.DEBUG_MODE,
    title="Knowledge Search",
    description="""Token Generation:\n 
    Please Use the below details on Postman to get the access token for API authorization. \n
    Request URL: `https://login-itg.external.hp.com/as/token.oauth2?grant_type=client_credentials`,\n
    Method: `Post`,\n
    Body: contains `client_id` and `client_secret` with enocding type `x-www-form-urlencoded`, \n""",
    summary="Knowledge Service acts as a unified gateway using OpenSearch to consolidate knowledge assets from various sources across HP IPS Service organization and presenting them through a single cohesive service layer for efficient and seamless access.",
    version="1.0.0",
    contact={
        "name": "Knowledge Search",
        "email": "knowlegesearch@hp.com",
    },
)

# Search API
subapp.include_router(core_search.router)

# ISearchUI Search Feedback API
subapp.include_router(core_auto_suggest.router)

# Render_link API
subapp.include_router(extras_kaas.router)
# Bulk render_link API
subapp.include_router(bulk_renderlink.router)


@subapp.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Invalid input. Please check the input parameters."},
    )


def register_middlewares(app: FastAPI):
    app.add_middleware(ExceptionHandlerMiddleware)
    app.add_middleware(AuthenticationMiddleware, backend=BearerTokenTenantAuthBackend())

    register_profiler_middlewares(app)


register_middlewares(subapp)
