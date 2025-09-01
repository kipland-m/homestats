# homestats - a dashboard to display local network information

## preview
![screenshot](https://github.com/user-attachments/assets/396bbd0a-6781-46a9-8bee-77ed92f79e69)

Running the project:

    host/frontend - python3 -m http.server 8001
	
    host/ - python3 -m uvicorn host.main:app --reload
	
    agent/ - python agent.py (for now, will become system tray level)

Components of the product
- Backend
	- FastAPI. Because yes
	- SQLite3 database
- Frontend
	- Browser based
- Agent
	- Python based system tray application that probably will interact with WSGI?

 Agent functionality
- Undecided on the language but maybe python.
- Lightweight, easily deployable agent that will be distributed to devices across your network.

Working on implementing sockets for communication between server and interface-
Naw screw all that lets do react slop for the frontend yes 👍
ok yes wait lets try NO LIBRARIES (for the frontend)

displaying simple response from the backend. next step i want to go ahead and spin up a sqlite server to store everything that comes in

agent sends data to API -> API stores data -> API sends data to frontend via websocket

using SQLite3, we are now storing stuff into the database as it comes in from the agent.
Got a nice looking frontend implemented, carding different agents in
