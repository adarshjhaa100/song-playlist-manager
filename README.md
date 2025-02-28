### Song Playlist Application

This application contains the following feature implemented as part of assignment at VivPro:

Backend:
  - Upload Song and Normalize
  - View all songs
  - Search for single song

Frontend:
  - List All songs
  - Search for single song
  - Sort columns
  - Export Current View



### Steps to Run the application:

**Backend:**
  - Create and activate virtualenv
      > python3 -m venv env
      > source env/bin/activate
  - Install requirements.txt
  -   > pip install requirements.txt
  - Make and Run Migrations
      > For syncing db changes
  - Run server: python manage.py runserver
  - Upload the given input json file. Can use the given curl:
    > curl --location 'http://127.0.0.1:8000/songs/upload/' \
--form 'file=@"/path/to/file"'

**Frontend**
  > cd into /song-playlist-ui
  > npm install
  > npm run dev
  - visit http://localhost:5173
