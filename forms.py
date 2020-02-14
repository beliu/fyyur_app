from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, AnyOf, URL, ValidationError, HostnameValidation
from wtforms.compat import string_types, text_type
from app import db, Artist, Venue
import re

# Custom validator for URL
class URL_Mod(URL):
    """
    Compares the incoming data to a sequence of valid inputs.
    :param values:
        A sequence of valid inputs.
    :param message:
        Error message to raise in case of a validation error. `%(values)s`
        contains the list of values.
    :param values_formatter:
        Function used to format the list of values in the error message.
    """
    def __init__(self, require_tld=True, message=None):
            regex = (
                r"(^[a-z]+://)?"
                r"www."
                r"(?P<host>[^\/\?:]+)"
                r"(?P<port>:[0-9]+)?"
                r"(?P<path>\/.*?)?"
                r"(?P<query>\?.*)?$"
            )
            super(URL, self).__init__(regex, re.IGNORECASE, message)
            self.validate_hostname = HostnameValidation(
                require_tld=require_tld, allow_ip=True
            )

# Custom validator for selecting multiple genres
class AnyOf_Multiple(AnyOf):
    """
    Compares the incoming data to a sequence of valid inputs.
    :param values:
        A sequence of valid inputs.
    :param message:
        Error message to raise in case of a validation error. `%(values)s`
        contains the list of values.
    :param values_formatter:
        Function used to format the list of values in the error message.
    """

    def __call__(self, form, field):
    
        if not set(field.data).issubset(self.values):
            message = self.message
            if message is None:
                message = field.gettext("Invalid value, must be one of: %(values)s.")

            raise ValidationError(
                message % dict(values=self.values_formatter(self.values))
            )

    @staticmethod   
    def default_values_formatter(values):
        return ", ".join(text_type(x) for x in values)

genre_keys = [
            ('Alternative'),
            ('Blues'),
            ('Classical'),
            ('Country'),
            ('Electronic'),
            ('Folk'),
            ('Funk'),
            ('Hip-Hop'),
            ('Heavy Metal'),
            ('Instrumental'),
            ('Jazz'),
            ('Musical Theatre'),
            ('Pop'),
            ('Punk'),
            ('R&B'),
            ('Reggae'),
            ('Rock n Roll'),
            ('Soul'),
            ('K-Pop'),
            ('Contemporary'),
            ('Indie'),
            ('Latin'),
            ('Other')
        ]

genre_choices = [
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('K-Pop', 'K-Pop'),
            ('Contemporary', 'Contemporary'),
            ('Indie', 'Indie'),
            ('Latin', 'Latin'),
            ('Other', 'Other')
        ]

state_keys = [
            ('AL'),
            ('AK'),
            ('AZ'),
            ('AR'),
            ('CA'),
            ('CO'),
            ('CT'),
            ('DE'),
            ('DC'),
            ('FL'),
            ('GA'),
            ('HI'),
            ('ID'),
            ('IL'),
            ('IN'),
            ('IA'),
            ('KS'),
            ('KY'),
            ('LA'),
            ('ME'),
            ('MT'),
            ('NE'),
            ('NV'),
            ('NH'),
            ('NJ'),
            ('NM'),
            ('NY'),
            ('NC'),
            ('ND'),
            ('OH'),
            ('OK'),
            ('OR'),
            ('MD'),
            ('MA'),
            ('MI'),
            ('MN'),
            ('MS'),
            ('MO'),
            ('PA'),
            ('RI'),
            ('SC'),
            ('SD'),
            ('TN'),
            ('TX'),
            ('UT'),
            ('VT'),
            ('VA'),
            ('WA'),
            ('WV'),
            ('WI'),
            ('WY')
        ]

state_choices = [
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY')
        ]

class ShowForm(FlaskForm):

    artist_id = SelectField(
        'artist_id',
        coerce=int,
        validators=[DataRequired()]
    )
    venue_id = SelectField(
        'venue_id',
        coerce=int,
        validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

    # Modify init so that shows can be created 
    # from newly added venues or artists
    def __init__(self, *args, **kwargs):
        # Get a list of artists
        artists = Artist.query.order_by(Artist.name).all()
        artist_choices = [(artist.id, artist.name) for artist in artists]
    
        # Get a list of venues
        venues = Venue.query.order_by(Venue.name).all()
        venue_choices = [(venue.id, venue.name) for venue in venues]

        super(ShowForm, self).__init__(*args, **kwargs)
        self.artist_id.choices = artist_choices
        self.venue_id.choices = venue_choices

        # return form

class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired(),
        AnyOf(state_keys)],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )

    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired(), 
        AnyOf_Multiple(genre_keys)],    # Using custom validator
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL_Mod()]    # Using custom validator
    )

class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        # TODO implement validation logic for state
        'state', validators=[DataRequired(),
        AnyOf(state_keys)],
        choices=state_choices
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired(),
        AnyOf_Multiple(genre_keys)],    # Using custom validator
        choices=genre_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL_Mod()]    # Using custom validator
    )

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM


