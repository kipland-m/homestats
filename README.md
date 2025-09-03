# homestats - a dashboard to display local network information

## preview
![screenshot](https://github.com/user-attachments/assets/396bbd0a-6781-46a9-8bee-77ed92f79e69)

Running the project:

    host/frontend - python3 -m http.server 8001
	
    host/ - python3 -m uvicorn host.main:app --reload
	
    agent/ - python agent.py (for now, will become system tray level)
	
defaultly running at http://0.0.0.0:8001/

Components of the product
- Backend
	- FastAPI
    - SQLite3 database
- Frontend
	- Browser based
    - Lightweight no library 
- Agent
	- Python based system tray application that probably will interact with WSGI?
        - have prototpe working with psutil.
    - Possible switching to Rust? I like the libraries from what I've seen. Would be fast to run in the background too.
    - Lightweight, easily deployable agent that will be distributed to devices across your network.

Working on implementing sockets for communication between server and frontend. Decided to do pure js, so as payloads from agents come into the backend, we will store them in the sqllite db, then instantly push them forward to the frontend via socket.

displaying simple response from the backend. next step i want to go ahead and spin up a sqlite server to store everything that comes in. 

using SQLite3, we are now storing stuff into the database as it comes in from the agent.
Got a nice looking frontend implemented, carding different agents in the main display
Next, I want to focus on getting more granular data, and getting a cool globe logo in the header.

Having some trouble getting extra network info. at least on mac, you need root access to get this. Why is it so hard to get insights about ur machine
