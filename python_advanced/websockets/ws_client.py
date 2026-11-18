#!/usr/bin/env python3
"""WebSocket client."""

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    response = await connect_and_send(
        "ws://localhost:8765", "Hello WebSocket"
    )
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
