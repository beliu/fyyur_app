from app import db, Artist, Venue, Show, format_datetime
import sys

groban = Artist.query.get(1)
mature_5 = Artist.query.get(2)
diablo_bull = Artist.query.get(3)
nail_in_coffin = Artist.query.get(4)
blake = Artist.query.get(5)
oos = Artist.query.get(6)
sara_braile = Artist.query.get(7)
ja_mon = Artist.query.get(8)

jezebel = Venue.query.get(1)
honkin_tonk = Venue.query.get(2)
lit = Venue.query.get(3)
trash_pit = Venue.query.get(4)
nice_traveler = Venue.query.get(5)
bk_life = Venue.query.get(6)
iron_lung = Venue.query.get(7)
skazle = Venue.query.get(8)
rum_drum = Venue.query.filter_by(name='The Rum Drum').one()

# show1 = Show(show_time=format_datetime('2020-02-23 10 PM'))
# show2 = Show(show_time=format_datetime('2020-04-21 8 PM'))
# show3 = Show(show_time=format_datetime('2020-02-14 7PM'))
# show4 = Show(show_time=format_datetime('2020-02-15 7PM'))
# show5 = Show(show_time=format_datetime('2020-03-08 9PM'))
# show6 = Show(show_time=format_datetime('2020-03-13 9:30PM'))
# show7 = Show(show_time=format_datetime('2020-04-22 10:15PM'))
# show8 = Show(show_time=format_datetime('2020-04-29 11PM'))
# show9 = Show(show_time=format_datetime('2020-05-03 11PM'))
# show10 = Show(show_time=format_datetime('2020-05-10 12AM'))
# show11 = Show(show_time=format_datetime('2020-05-15 7:45PM'))
# show12 = Show(show_time=format_datetime('2020-05-30 9:15PM'))
# show13 = Show(show_time=format_datetime('2020-06-02 11PM'))
# show14 = Show(show_time=format_datetime('2020-06-16 10PM'))
# show15 = Show(show_time=format_datetime('2020-06-29 8:30PM'))
show16 = Show(show_time=format_datetime('2020-07-04 10PM'))
show17 = Show(show_time=format_datetime('2020-07-11 10PM'))


# show1.venue = trash_pit
# show2.venue = skazle
# show3.venue = jezebel
# show4.venue = jezebel
# show5.venue = lit
# show6.venue = bk_life
# show7.venue = iron_lung
# show8.venue = lit
# show9.venue = bk_life
# show10.venue = bk_life
# show11.venue = lit
# show12.venue = jezebel
# show13.venue = jezebel
# show14.venue = nice_traveler
# show15.venue = honkin_tonk

# show5.artist = diablo_bull
# show6.artist = diablo_bull
# show7.artist = nail_in_coffin
# show8.artist = blake
# show9.artist = blake
# show10.artist = blake
# show11.artist = oos
# show12.artist = oos
# show13.artist = oos
# show14.artist = sara_braile
# show15.artist = sara_braile

# groban.shows = [show1, show2]
# sara_braile.shows = [show3]
# mature_5.shows = [show4]
# diablo_bull.shows = [show5, show6]
# nail_in_coffin.shows = [show7]
# blake = [show8, show9, show10]
# oos = [show11, show12, show13]
# sara_braile = [show14, show15]

rum_drum.shows = [show16, show17]

with db.session.no_autoflush:
    ja_mon.shows = [show16, show17]

try:
    # db.session.add(show1)
    # db.session.add(show2)
    # db.session.add(show3)
    # db.session.add(show4)
    # db.session.add(show5)
    # db.session.add(show6)
    # db.session.add(show7)
    # db.session.add(show8)
    # db.session.add(show9)
    # db.session.add(show10)
    # db.session.add(show11)
    # db.session.add(show12)
    # db.session.add(show13)
    # db.session.add(show14)
    # db.session.add(show15)
    # db.session.add(show16)
    # db.session.add(show17)
    # db.session.commit()
except:
    db.session.rollback()
    print(sys.exc_info())
    
finally:
    db.session.close()
