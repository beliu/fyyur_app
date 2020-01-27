from app import db, Venue, Venue_Genre
import sys

jezebel_lair = Venue(
    name='Jezebel\'s Lair',
    city='New York',
    state='NY',
    address='18E 58th St.',
    website='www.jezeli.com',
    phone='212-304-3394',
    image_link='www.jezeli.com/pic',
    facebook_link='www.facebook.com/jezebel_lair'
)

jezebel_lair_genre1 = Venue_Genre(genre='Indie')
jezebel_lair_genre2 = Venue_Genre(genre='Jazz')
jezebel_lair_genre1.venue = jezebel_lair
jezebel_lair_genre2.venue = jezebel_lair


honkin_tonk = Venue(
    name='The Honkin Tonk Pub',
    city='Nashville',
    state='TN',
    address='394 Brooksfield Rd.',
    website='www.honkintonkpub.com',
    phone='615-349-1239',
    image_link='www.honkintonkpub.com/pic',
    facebook_link='www.facebook.com/honkin_tonk'
)

honkin_tonk_genre1 = Venue_Genre(genre='Country')
honkin_tonk_genre2 = Venue_Genre(genre='Rock')
honkin_tonk_genre1.venue = honkin_tonk
honkin_tonk_genre2.venue = honkin_tonk


lit = Venue(
    name='LIT',
    city='Los Angeles',
    state='CA',
    address='55E Tulsa St.',
    phone='323-292-1348',
    website='www.lit.com',
    image_link='www.lit.com/profile',
    facebook_link='www.facebook.com/lit'
)

lit_genre1 = Venue_Genre(genre='Hip Hop')
lit_genre2 = Venue_Genre(genre='Dance')
lit_genre1.venue = lit
lit_genre2.venue = lit


trash_pit = Venue(
    name='Trash Pit',
    city='Los Angeles',
    state='CA',
    address='12 Wooling Dr.',
    phone='323-123-4845',
    website='www.trashpit.com',
    image_link='www.trashpit.com/image',
    facebook_link='www.facebook.com/trash_pit'
)

trash_pit_genre1 = Venue_Genre(genre='Metal')
trash_pit_genre1.venue = trash_pit


nice_traveler = Venue(
    name='Nice Traveler Lounge',
    city='New York',
    state='NY',
    address='16E W 15th St.',
    phone='212-384-0013',
    website='www.nicetraveler.com',
    image_link='www.nicetraveler.com/pic',
    facebook_link='www.facebook.com/nice_traveler'
)

nice_traveler_genre1 = Venue_Genre(genre='Indie')
nice_traveler_genre2 = Venue_Genre(genre='Jazz')
nice_traveler_genre1.venue = nice_traveler
nice_traveler_genre2.venue = nice_traveler


bk_life = Venue(
    name='That BK Life',
    city='New York',
    state='NY',
    address='12 84th St.',
    phone='718-148-2323',
    website='www.thatbklife.com',
    image_link='www.thatbklife.com/pic',
    facebook_link='www.facebook.com/bk_life'
)

bk_life_genre1 = Venue_Genre(genre='Hip Hop')
bk_life_genre1.venue = bk_life


iron_lung = Venue(
    name='Iron Lung',
    city='San Francisco',
    state='CA',
    address='127 Furthing St.',
    phone='415-625-0011',
    website='www.ironlung.com',
    image_link='www.ironlung.com/pic',
    facebook_link='www.facebook.com/iron_lung'
)

iron_lung_genre1 = Venue_Genre(genre='Metal')
iron_lung_genre2 = Venue_Genre(genre='Rock')
iron_lung_genre1.venue = iron_lung
iron_lung_genre2.venue = iron_lung


skazle = Venue(
    name='Skazle',
    city='Seattle',
    state='WA',
    address='96 Instance St.',
    phone='564-483-5781',
    website='www.skazle.com',
    image_link='www.skazle.com/image',
    facebook_link='www.facebook.com/skazle'
)

skazle_genre1 = Venue_Genre(genre='Indie')
skazle_genre2 = Venue_Genre(genre='Rock')
skazle_genre1.venue = skazle
skazle_genre2.venue = skazle


rum_drum = Venue(
    name='The Rum Drum',
    city='Miami',
    state='FL',
    address='12 Palm Terrace Rd.',
    phone='315-003-3948',
    website='www.rumdrum.com',
    image_link='www.rumdrum.com/profile',
    facebook_link='www.facebook.com/rum_drum'
)

rum_drum_genre1 = Venue_Genre(genre='Regae')
rum_drum_genre2 = Venue_Genre(genre='Latin')
rum_drum_genre1.venue = rum_drum
rum_drum_genre2.venue = rum_drum


try:
    db.session.add(jezebel_lair)
    db.session.add(honkin_tonk)
    db.session.add(lit)
    db.session.add(trash_pit)
    db.session.add(nice_traveler)
    db.session.add(iron_lung)
    db.session.add(skazle)
    db.session.add(rum_drum)
    db.session.add(bk_life)
    db.session.commit()
except:
    db.session.rollback()
    print(sys.exc_info())
finally:
    db.session.close()