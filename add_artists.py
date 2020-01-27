from app import db, Artist, Artist_Genre
import sys

# Add artist data
groban = Artist(
  name='Groban',
  city='New York',
  state='NY',
  phone='212-121-3940',
  website='www.groban.com',
  image_link='www.groban.com/img',
  facebook_link='www.facebook.com/groban'
)

groban_genre1 = Artist_Genre(genre='rock')
groban_genre2 = Artist_Genre(genre='contemporary')
groban_genre1.artist = groban
groban_genre2.artist = groban


mature_five = Artist(
  name='Mature 5',
  city='New York',
  state='NY',
  phone='212-304-2399',
  website='www.maturefive.com',
  image_link='www.maturefive.com/img',
  facebook_link='www.facebook.com/mature_five'
)

mature_five_genre1 = Artist_Genre(genre='pop')
mature_five_genre2 = Artist_Genre(genre='contemporary')

mature_five_genre1.artist = mature_five
mature_five_genre2.artist = mature_five


diablo_bull = Artist(
  name='Diablo Bull',
  city='Miami',
  state='FL',
  phone='305-193-4584',
  website='www.eldiablobull.com',
  image_link='www.eldiablobull.com/pic',
  facebook_link='www.facebook.com/diablo_bull'
)

diablo_bull_genre1 = Artist_Genre(genre='hip hop')
diablo_bull_genre2 = Artist_Genre(genre='latin')

diablo_bull_genre1.artist = diablo_bull
diablo_bull_genre2.artist = diablo_bull


nail_in_coffin = Artist(
  name='Nail in the Coffin',
  city='Seattle',
  state='WA',
  phone='564-908-1827',
  website='www.nailincoffin.com',
  image_link='www.nailincoffin.com/profile',
  facebook_link='www.facebook.com/nail_in_coffin'
)

nail_in_coffin_genre1 = Artist_Genre(genre='metal')
nail_in_coffin_genre1.artist = nail_in_coffin


blake = Artist(
  name='Blake',
  city='San Francisco',
  state='CA',
  phone='415-783-0394',
  website='www.thisisblake.com',
  image_link='www.thisisblake.com/img',
  facebook_link='www.facebook.com/blake'
)

blake_genre1 = Artist_Genre(genre='hip hop')
blake_genre1.artist = blake

oos = Artist(
  name='OOS',
  city='Syracuse',
  state='NY',
  phone='315-988-1847',
  website = 'www.outofschool.com',
  image_link='www.outofschool.com/img',
  facebook_link='www.facebook.com/oos'
)

oos_genre1 = Artist_Genre(genre='k-pop')
oos_genre2 = Artist_Genre(genre='pop')
oos_genre3 = Artist_Genre(genre='electronic')

oos_genre1.artist = oos
oos_genre2.artist = oos
oos_genre3.artist = oos

sara_braile = Artist(
  name='Sara Braile',
  city='San Francisco',
  state='CA',
  phone='415-304-2390',
  website = 'www.braile.com',
  image_link='www.braile.com/img',
  facebook_link='www.facebook.com/sara_braile'
)

sara_braile_genre1 = Artist_Genre(genre='indie')
sara_braile_genre2 = Artist_Genre(genre='contemporary')
sara_braile_genre3 = Artist_Genre(genre='jazz')

sara_braile_genre1.artist = sara_braile
sara_braile_genre2.artist = sara_braile
sara_braile_genre2.artist = sara_braile


ja_mon = Artist(
  name='Ja Mon',
  city='New York',
  state='NY',
  phone='212-391-2038',
  website = 'www.jamon.com',
  image_link='www.jamon.com/img',
  facebook_link='www.facebook.com/ja_mon'
)

ja_mon_genre1 = Artist_Genre(genre='regae')
ja_mon_genre1.artist = ja_mon


try:
    db.session.add(groban)
#   db.session.add(diablo_bull)
#   db.session.add(mature_five)
#   db.session.add(nail_in_coffin)
#   db.session.add(blake)
#   db.session.add(oos)
#   db.session.add(sara_braile)
#   db.session.add(ja_mon)
    db.session.commit()
except:
    db.session.rollback()
    print(sys.exc_info())
finally:
    db.session.close()
