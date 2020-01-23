from app import db, Artist, Artist_Genre, Venue, Venue_Genre, Show
from dateutil.parser import parse
import sys

### ----            Add a Venue and Genre           --- ###
# venue1 = Venue(name='Jezebel\'s Lair',
#                city='Los Angeles',
#                state='CA',
#                address='321 Santa Monica Blvd.',
#                phone='213-456-3819',
#                image_link='www.jezeli.com/pic',
#                facebook_link='www.facebook.com/jezebel_lair')

# venue_genre1 = Venue_Genre(genre='rock')
# venue_genre1.venue = venue1

# try:
#     db.session.add(venue1)
#     db.session.add(venue_genre1)
#     db.session.commit()
# except:
#     db.session.rollback()
#     print(sys.exc_info)
# finally:
#     db.session.close()

### ----            Add a Show           --- ###
# artist1 = Artist.query.get(1)
# venue1 = Venue.query.get(1)

# show_time = parse('2020-01-20 8:00PM')

# show1 = Show(show_time=show_time)
# show1.artist = artist1
# show1.venue = venue1

# try:
#     db.session.add(show1)
#     db.session.commit()
# except:
#     db.session.rollback()
#     print(sys.exc_info())
# finally:
#     show1 = Show.query.get(3)
#     show1.show_time.time().strftime('%I:%M %p')
#     db.session.close()
    