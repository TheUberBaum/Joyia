import asyncio
import websockets

async def connect_to_server():
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Send a message to the server
        message = "Hello, WebSocket server!"
        await websocket.send(message)

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Server response: {response}")

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(connect_to_server())

