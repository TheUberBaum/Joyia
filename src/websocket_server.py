import asyncio
import websockets

# Define a function to handle WebSocket connections
async def handle_connection(websocket, path):
    try:
        # You can put your WebSocket logic here
        while True:
            message = await websocket.recv()
            # Handle the received message
            print(f"Received message: {message}")
            # Send a response back to the client
            response = f"Server received: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        # Handle the case when the client disconnects
        print("Client disconnected")

# Create the WebSocket server
start_server = websockets.serve(handle_connection, "localhost", 8765)

if __name__ == '__main__':
    # Start the WebSocket server
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

