# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
import logging

from fastapi import FastAPI

from app.db import init_db
from app.api import ping, summaries

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )  # new

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
