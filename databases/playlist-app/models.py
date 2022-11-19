"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    id = SERIAL PRIMARY KEY,
    name = StringField('Name', [validators.Length(min=1,max=25)]),
    description = StringField('Description', [validator.Length(min=1,max=150)]),
    



class Song(db.Model):
    """Song."""
    id = SERIAL PRIMARY KEY,
    playlist_id,
    song_id
    


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    id = SERIAL PRIMARY KEY,
    title = StringField('Title', [validators.length(min=1,max=50)])


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
