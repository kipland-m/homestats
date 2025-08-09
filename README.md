# homestats - a dashboard to display local network information

Components of the product
- Backend
	- FastAPI. Because yes
- Frontend
	- Browser based
- Agent
	- Python based system tray application that probably will interact with WSGI?

 Agent functionality
- Undecided on the language but maybe python.
- Lightweight, easily deployable agent that will be distributed to devices across your network.
- 

Working on implementing sockets for communication between server and interface-

Naw screw all that lets do react slop for the frontend yes 👍
ok yes wait lets try NO LIBRARIES (for the frontend)

displaying simple response from the backend. next step i want to go ahead and spin up a sqlite server to store everything that comes in

agent sends data to API -> API stores data -> API sends data to frontend via websocket
