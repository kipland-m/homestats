# Kipland Melton 2025
# create window for custom display to run on CCTV monitor

import pygame
import asyncio
import websockets

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.Font(None, 72)
pygame.display.set_caption("lets monitor shit")

# Function to handle the chat client
async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
        while True:
            # Prompt the user for a message
            message = input("Enter message: ")
            # Send the message to the server
            await websocket.send(message)
            # Receive a message from the server
            response = await websocket.recv()
            print(f"Received: {response}")

# Run the client
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        text = font1.render("Test text", True, (155,155,155))
        screen.blit(text, (50, 50))


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(chat())
    main()
