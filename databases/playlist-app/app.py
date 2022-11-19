from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField)
from wtforms.validators import InputRequired, Length

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    updated_playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
    }
    # set the former playlist to the new one we just updated/edited
    playlist.update_one(
        {'_id': ObjectId(playlist_id)},
        {'$set': updated_playlist})
    # take us back to the playlist's show page
    return redirect(url_for('playlists_show', playlist_id=playlist_id))


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    if request.method=='POST':
    


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    show_song = {
        'title': request.form.get('title'),
        'artist': request.form.get('artist'),
    }
    # take us back to the playlist's show page
    return redirect(url_for('songs', song_id=song_id))



@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    form =RegisterForm(request.form)
	if request.method=='POST' and form.validate():
		name=form.name.data
        playlist_id=form.playlist_id.data
        song_id=form.song_id.data


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

  playlist = Playlist.query.get_or_404(playlist_id)
  form = NewSongForPlaylistForm()

  # Restrict form to songs not already on this playlist

  curr_on_playlist = [s.id for s in playlist.songs]
  form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(curr_on_playlist))
                      .all())

  if form.validate_on_submit():
    app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
    def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

  playlist = Playlist.query.get_or_404(playlist_id)
  form = NewSongForPlaylistForm()

  # Restrict form to songs not already on this playlist

  curr_on_playlist = [s.id for s in playlist.songs]
  form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(curr_on_playlist))
                      .all())

  if form.validate_on_submit():

      # This is one way you could do this ...
      playlist_song = PlaylistSong(song_id=form.song.data,
                                  playlist_id=playlist_id)
      db.session.add(playlist_song)

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
