from app import db, Artist, Artist_Genre
import sys

# Add artist data
artist1 = Artist(
  name='Mature 5',
  city='New York',
  state='NY',
  phone='212-304-2399',
  image_link='www.maturefive.com/img',
  facebook_link='www.facebook.com/mature_five'
)

artist1_genre1 = Artist_Genre(genre='pop')
artist1_genre2 = Artist_Genre(genre='contemporary')

artist1_genre1.artist = artist1
artist1_genre2.artist = artist1


artist2 = Artist(
  name='Diablo Bull',
  city='Miami',
  state='FL',
  phone='305-193-4584',
  image_link='www.eldiablobull.com/pic',
  facebook_link='www.facebook.com/diablo_bull'
)

artist2_genre1 = Artist_Genre(genre='hip hop')
artist2_genre2 = Artist_Genre(genre='latin')

artist2_genre1.artist = artist2
artist2_genre2.artist = artist2


artist3 = Artist(
  name='Nail in the Coffin',
  city='Seattle',
  state='WA',
  phone='564-908-1827',
  image_link='www.nailincoffin.com/profile',
  facebook_link='www.facebook.com/nail_in_coffin'
)

artist3_genre1 = Artist_Genre(genre='metal')
artist3_genre1.artist = artist3


artist4 = Artist(
  name='Blake',
  city='San Francisco',
  state='CA',
  phone='415-783-0394',
  image_link='www.thisisblake.com/img',
  facebook_link='www.facebook.com/blake'
)

artist4_genre1 = Artist_Genre(genre='hip hop')
artist4_genre1.artist = artist4

artist5 = Artist(
  name='OOS',
  city='Syracuse',
  state='NY',
  phone='315-988-1847',
  image_link='www.outofschool.com/img',
  facebook_link='www.facebook.com/oos'
)

artist5_genre1 = Artist_Genre(genre='k-pop')
artist5_genre2 = Artist_Genre(genre='pop')
artist5_genre3 = Artist_Genre(genre='electronic')

artist5_genre1.artist = artist5
artist5_genre2.artist = artist5
artist5_genre3.artist = artist5

artist6 = Artist(
  name='Sara Braile',
  city='San Francisco',
  state='CA',
  phone='415-304-2390',
  image_link='www.braile.com/img',
  facebook_link='www.facebook.com/sara_braile'
)

artist6_genre1 = Artist_Genre(genre='indie')
artist6_genre2 = Artist_Genre(genre='contemporary')
artist6_genre3 = Artist_Genre(genre='jazz')

artist6_genre1.artist = artist6
artist6_genre2.artist = artist6
artist6_genre2.artist = artist6


artist7 = Artist(
  name='Ja Mon',
  city='New York',
  state='NY',
  phone='212-391-2038',
  image_link='www.jamon.com/img',
  facebook_link='www.facebook.com/ja_mon'
)

artist7_genre1 = Artist_Genre(genre='regae')
artist7_genre1.artist = artist7


try:
  db.session.add(artist1)
  db.session.add(artist2)
  db.session.add(artist3)
  db.session.add(artist4)
  db.session.add(artist5)
  db.session.add(artist6) 
  db.session.commit()
except:
  db.session.rollback()
  print(sys.exc_info())
finally:
  db.session.close()
