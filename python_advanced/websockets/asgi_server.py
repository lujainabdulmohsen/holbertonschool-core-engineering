#!/usr/bin/env python3
"""ASGI WebSocket echo server with browser client."""

from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect

BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    return FileResponse(BASE_DIR / "index.html")


async def stylesheet(request):
    return FileResponse(BASE_DIR / "styles.css", media_type="text/css")


async def javascript(request):
    return FileResponse(
        BASE_DIR / "chat.js", media_type="application/javascript"
    )


async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    Route("/styles.css", stylesheet),
    Route("/chat.js", javascript),
    WebSocketRoute("/ws", websocket_endpoint),
])
