from app import db, Venue, Venue_Genre
import sys

venue1 = Venue(
    name='The Honkin Tonk Pub',
    city='Nashville',
    state='TN',
    address='394 Brooksfield Rd.',
    phone='615-349-1239',
    image_link='www.honkintonkpub.com',
    facebook_link='www.facebook.com/honkin_tonk'
)

venue1_genre1 = Venue_Genre(genre='Country')
venue1_genre2 = Venue_Genre(genre='Rock')
venue1_genre1.venue = venue1
venue1_genre2.venue = venue1


venue2 = Venue(
    name='LIT',
    city='Los Angeles',
    state='CA',
    address='55E Tulsa St.',
    phone='323-292-1348',
    image_link='www.lit.com',
    facebook_link='www.facebook.com/lit'
)

venue2_genre1 = Venue_Genre(genre='Hip Hop')
venue2_genre2 = Venue_Genre(genre='Dance')
venue2_genre1.venue = venue2
venue2_genre2.venue = venue2


venue3 = Venue(
    name='Trash Pit',
    city='Los Angeles',
    state='CA',
    address='12 Wooling Dr.',
    phone='323-123-4845',
    image_link='www.trashpit.com',
    facebook_link='www.facebook.com/trash_pit'
)

venue3_genre1 = Venue_Genre(genre='Metal')
venue3_genre1.venue = venue3


venue4 = Venue(
    name='Nice Traveler Lounge',
    city='New York',
    state='NY',
    address='16E W 15th St.',
    phone='212-384-0013',
    image_link='www.nicetraveler.com',
    facebook_link='www.facebook.com/nice_traveler'
)

venue4_genre1 = Venue_Genre(genre='Indie')
venue4_genre2 = Venue_Genre(genre='Jazz')
venue4_genre1.venue = venue4
venue4_genre2.venue = venue4


venue5 = Venue(
    name='That BK Life',
    city='New York',
    state='NY',
    address='12 84th St.',
    phone='718-148-2323',
    image_link='www.thatbklife.com',
    facebook_link='www.facebook.com/bk_life'
)

venue5_genre1 = Venue_Genre(genre='Hip Hop')
venue5_genre1.venue = venue5


venue6 = Venue(
    name='Iron Lung',
    city='San Francisco',
    state='CA',
    address='127 Furthing St.',
    phone='415-625-0011',
    image_link='www.ironlung.com',
    facebook_link='www.facebook.com/iron_lung'
)

venue6_genre1 = Venue_Genre(genre='Metal')
venue6_genre2 = Venue_Genre(genre='Rock')
venue6_genre1.venue = venue6
venue6_genre2.venue = venue6


venue7 = Venue(
    name='Skazle',
    city='Seattle',
    state='WA',
    address='96 Instance St.',
    phone='564-483-5781',
    image_link='www.skazle.com',
    facebook_link='www.facebook.com/skazle'
)

venue7_genre1 = Venue_Genre(genre='Indie')
venue7_genre2 = Venue_Genre(genre='Rock')
venue7_genre1.venue = venue7
venue7_genre2.venue = venue7


venue8 = Venue(
    name='The Rum Drum',
    city='Miami',
    state='FL',
    address='12 Palm Terrace Rd.',
    phone='315-003-3948',
    image_link='www.rumdrum.com',
    facebook_link='www.facebook.com/rum_drum'
)

venue8_genre1 = Venue_Genre(genre='Regae')
venue8_genre2 = Venue_Genre(genre='Latin')
venue8_genre1.venue = venue8
venue8_genre2.venue = venue8


try:
    db.session.add(venue1)
    db.session.add(venue2)
    db.session.add(venue3)
    db.session.add(venue4)
    db.session.add(venue5)
    db.session.add(venue6)
    db.session.add(venue7)
    db.session.add(venue8)
    db.session.commit()
except:
    db.session.rollback()
    print(sys.exc_info())
finally:
    db.session.close()