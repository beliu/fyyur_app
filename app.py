#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import FlaskForm
from forms import *
import datetime
from wtforms.validators import ValidationError
import sys
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config.DefaultConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(500), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120))
    genres = db.relationship('Venue_Genre', backref='venue',
                                    lazy=True, cascade='all, delete-orphan')
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    shows = db.relationship('Show', backref='venue',
                            lazy='select', cascade='all, delete-orphan')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(500), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120))
    genres = db.relationship('Artist_Genre', backref='artist',
                                    lazy=True, cascade='all, delete-orphan')
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    shows = db.relationship('Show', backref='artist',
                            lazy='select', cascade='all, delete-orphan')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

# These Genre tables allow an artist or venue 
# to be associated with multiple genres
class Artist_Genre(db.Model):
    __tablename__ = 'artist_genre'

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'),
                          nullable=False, primary_key=True)
    genre = db.Column(db.String(), nullable=False, primary_key=True)

class Venue_Genre(db.Model):
    __tablename__ = 'venue_genre'

    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'),
                          nullable=False, primary_key=True)
    genre = db.Column(db.String(), nullable=False, primary_key=True)

# The Show table, that is a child of Artist and Venue
class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), 
                          nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'),
                         nullable=False)
    show_time = db.Column(db.DateTime, nullable=False)


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime


#----------------------------------------------------------------------------#
# Helper Functions.
#----------------------------------------------------------------------------#
def get_upcoming_shows(table, id, return_count=True):
  # Get the number of upcoming shows
  query = db.session.query(table.id, table.name, table.image_link, 
                           Show.id, Show.show_time)
  query = query.join(Show)
  num_upcoming_shows = query.filter(
      table.id == id,
      Show.show_time > datetime.datetime.now()
  )
  
  if return_count:
    return num_upcoming_shows.count()
  
  return num_upcoming_shows.all()

def get_past_shows(table, id, return_count=True):
  # Get the number of upcoming shows
  query = db.session.query(table.id, table.name, table.image_link, 
                           Show.id, Show.show_time)
  query = query.join(Show)
  num_past_shows = query.filter(
      table.id == id,
      Show.show_time < datetime.datetime.now()
  )
  
  if return_count:
    return num_past_shows.count()
  
  return num_past_shows.all()


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  print('Testing redirect to homepage')
  return render_template('pages/home.html')


#  ----------------------------------------------------------------
#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  
  # Get a list of unique areas (i.e. city + state) from the Venues records
  areas = Venue.query.distinct('state', 'city').all()

  # Extract venue data from each area
  data = []
  for area in areas:
    area_dict = {
      'city': area.city,
      'state': area.state
    }
    
    venues = Venue.query.filter_by(state=area.state, city=area.city).all()
    venues_data = []
    for venue in venues:
        num_upcoming_shows = get_upcoming_shows(Venue, venue.id)

        venue_dict = {
        'id': venue.id,
        'name': venue.name,
        'num_upcoming_shows': num_upcoming_shows
        }
        venues_data.append(venue_dict)

    # Add venue info to each area  
    area_dict['venues'] = venues_data
    data.append(area_dict)

  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"

  search_term = request.form.get('search_term', '')
  results = Venue.query.filter(Venue.name.ilike('%' + search_term + '%')).all()

  data = []
  for venue in results:
    num_upcoming_shows = get_upcoming_shows(Venue, venue.id)
    venue_info = {
      "id": venue.id,
      "name": venue.name,
      "num_upcoming_shows": num_upcoming_shows
    }
    data.append(venue_info)

  response={
    "count": len(results),
    "data": data
  }

  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id

  # See if this venue exists
  venue = Venue.query.get(venue_id)
  if venue is None:
    abort(400)
  
  # Find venue genres
  query = Venue_Genre.query.join(Venue)
  venue_results = query.filter(Venue.id == venue_id).all()
  genres = [result.genre for result in venue_results]

  # Query for past and upcoming shows
  query = db.session.query(Artist, Show).join(Show).join(Venue)

  # Find past shows
  past_shows = []
  show_results = (query.filter(Venue.id == venue_id, 
                  Show.show_time < datetime.datetime.now())
                  .order_by(Show.show_time.desc()).all())
  
  for result in show_results:
    artist = result[0]
    show = result[1]
    show_dict = {
      "artist_id": artist.id,
      "artist_name": artist.name,
      "artist_image_link": artist.image_link,
      "start_time": datetime.datetime.strftime(show.show_time, '%Y-%m-%d %I:%M%p')
    }
    past_shows.append(show_dict)

  # Find upcoming shows
  upcoming_shows = []
  show_results = (query.filter(Venue.id == venue_id, 
                  Show.show_time > datetime.datetime.now())
                  .order_by(Show.show_time).all())
  
  for result in show_results:
    artist = result[0]
    show = result[1]
    show_dict = {
      "artist_id": artist.id,
      "artist_name": artist.name,
      "artist_image_link": artist.image_link,
      "start_time": datetime.datetime.strftime(show.show_time, '%Y-%m-%d %I:%M%p')
    }
    upcoming_shows.append(show_dict)

  data = {
    "id": venue.id,
    "name": venue.name,
    "genres": genres,
    "address": venue.address,
    "city": venue.city,
    "state": venue.state,
    "phone": venue.phone,
    "website": venue.website,
    "facebook_link": venue.facebook_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description": venue.seeking_description,
    "image_link": venue.image_link,
    "past_shows": past_shows,
    "upcoming_shows": upcoming_shows,
    "past_shows_count": len(past_shows),
    "upcoming_shows_count": len(upcoming_shows),
  }

  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()  
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  form = VenueForm()

  # Create a new venu record
  new_venue = Venue(
    name = form.name.data,
    city = form.city.data,
    state = form.state.data,
    address = form.address.data,
    website = '',
    phone = form.phone.data,
    image_link = '',
    facebook_link = form.facebook_link.data,
    seeking_talent = False,
    seeking_description = ''
  )

  for genre in form.genres.data:
    venue_genre = Venue_Genre(genre=genre)
    venue_genre.venue = new_venue

  error = False    # Error flag for db insert
  try:
    assert form.validate_on_submit()
    db.session.add(new_venue)
    db.session.commit()
  except:
    db.session.rollback()
    print(sys.exc_info())
    error = True
  finally:
    db.session.close()

  # on successful db insert, flash success
  if not error:
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
  elif not form.validate_on_submit():
    # TODO: on unsuccessful db insert, flash an error instead.
    flash('An error occurred when filling out the form. Venue ' 
           + request.form['name'] + ' could not be listed.')
  else:
    flash('An internal database error occurred. Venue ' 
           + request.form['name'] + ' could not be listed.')

  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  venue = Venue.query.get(venue_id)
  venue_name = venue.name

  error = False
  try:
    db.session.delete(venue)
    db.session.commit()
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  
  if error:
    flash(f'An error occurred. Venue {venue_name} was not deleted.')
  else:
    flash(f'{venue_name} was successfully deleted.')
  
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
 
  return jsonify({'venue_name': venue_name})

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  artists = Artist.query.all()
  data = []
  for artist in artists:
    artist_shows = get_upcoming_shows(Artist, artist.id)
    artist_info = {
      "id": artist.id,
      "name": artist.name,
      "num_upcoming_shows": artist_shows
    }
    data.append(artist_info)

  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".

  search_term = request.form.get('search_term', '')
  artists = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()
  artists_count = len(artists)

  data = []
  for artist in artists:
    artist_shows = get_upcoming_shows(Artist, artist.id)
    artist_info = {
      "id": artist.id,
      "name": artist.name,
      "num_upcoming_shows": artist_shows
    }
    data.append(artist_info)

  response = {
    "count": artists_count,
    "data": data
  }

  return render_template('pages/search_artists.html', results=response, 
                         search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # TODO: replace with real artist data from the artists table, using artist_id
  artist = Artist.query.get(artist_id)

  # Get artist genres
  query = Artist_Genre.query.join(Artist)
  genre_results = query.filter(Artist.id == artist_id).all()
  genres = [result.genre for result in genre_results]

  # Joint query to get information about past and upcoming shows
  query = db.session.query(Venue, Show).join(Show).join(Artist)

  # Get artist past shows
  past_shows = []
  show_results = (query.filter(Artist.id == artist_id, 
                  Show.show_time < datetime.datetime.now())
                  .order_by(Show.show_time.desc()).all())

  for result in show_results:
    venue = result[0]
    show = result[1]
    show_dict = {
      "venue_id": venue.id,
      "venue_name": venue.name,
      "venue_image_link": venue.image_link,
      "start_time": datetime.datetime.strftime(show.show_time, '%Y-%m-%d %I:%M%p')
    }
    past_shows.append(show_dict)

  # Get artist upcoming shows
  upcoming_shows = []
  show_results = (query.filter(Artist.id == artist_id,
                  Show.show_time > datetime.datetime.now())
                  .order_by(Show.show_time).all())
  
  for result in show_results:
    venue = result[0]
    show = result[1]
    show_dict = {
      "venue_id": venue.id,
      "venue_name": venue.name,
      "venue_image_link": venue.image_link,
      "start_time": datetime.datetime.strftime(show.show_time, '%Y-%m-%d %I:%M%p')
    }
    upcoming_shows.append(show_dict)

  data = {
    "id": artist.id,
    "name": artist.name,
    "genres": genres,
    "city": artist.city,
    "state": artist.state,
    "phone": artist.phone,
    "website": artist.website,
    "facebook_link": artist.facebook_link,
    "seeking_venue": artist.seeking_venue,
    "seeking_description": artist.seeking_description,
    "past_shows": past_shows,
    "upcoming_shows": upcoming_shows,
    "past_shows_count": len(past_shows),
    "upcoming_shows_count": len(upcoming_shows)
  }

  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist={
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
  }
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue={
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
  }
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion

  # on successful db insert, flash success
  flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  data=[{
    "venue_id": 1,
    "venue_name": "The Musical Hop",
    "artist_id": 4,
    "artist_name": "Guns N Petals",
    "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "start_time": "2019-05-21T21:30:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 5,
    "artist_name": "Matt Quevedo",
    "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
  }]
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead

  # on successful db insert, flash success
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
