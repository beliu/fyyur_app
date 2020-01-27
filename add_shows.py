from app import db, Artist, Venue, Show, format_datetime
import sys

groban = Artist.query.filter(Artist.name.ilike('%groban')).one()
mature_5 = Artist.query.filter(Artist.name.ilike('%mature%')).one()
diablo_bull = Artist.query.filter(Artist.name.ilike('%diablo%')).one()
nail_in_coffin = Artist.query.filter(Artist.name.ilike('%nail%')).one()
blake = Artist.query.filter(Artist.name.ilike('%blake%')).one()
oos = Artist.query.filter(Artist.name.ilike('%oos%')).one()
sara_braile = Artist.query.filter(Artist.name.ilike('%sara%')).one()
ja_mon = Artist.query.filter(Artist.name.ilike('%ja mon%')).one()

jezebel = Venue.query.filter(Venue.name.ilike('%jezebel%')).one()
honkin_tonk = Venue.query.filter(Venue.name.ilike('%honkin%')).one()
lit = Venue.query.filter(Venue.name.ilike('%lit%')).one()
trash_pit = Venue.query.filter(Venue.name.ilike('%trash_pit%')).one()
nice_traveler = Venue.query.filter(Venue.name.ilike('%nice%')).one()
bk_life = Venue.query.filter(Venue.name.ilike('%bk%')).one()
iron_lung = Venue.query.filter(Venue.name.ilike('%iron%')).one()
skazle = Venue.query.filter(Venue.name.ilike('%skazle%')).one()
rum_drum = Venue.query.filter(Venue.name.ilike('%rum%')).one()

# show1 = Show(show_time=format_datetime('2019-02-23 10 PM'))
# show2 = Show(show_time=format_datetime('2019-04-21 8 PM'))
# show3 = Show(show_time=format_datetime('2019-02-14 7PM'))
# show4 = Show(show_time=format_datetime('2019-02-15 7PM'))
# show5 = Show(show_time=format_datetime('2019-03-08 9PM'))
# show6 = Show(show_time=format_datetime('2019-03-13 9:30PM'))
# show7 = Show(show_time=format_datetime('2019-04-22 10:15PM'))
# show8 = Show(show_time=format_datetime('2019-04-29 11PM'))
# show9 = Show(show_time=format_datetime('2019-05-03 11PM'))
# show10 = Show(show_time=format_datetime('2019-05-10 12AM'))
# show11 = Show(show_time=format_datetime('2019-05-15 7:45PM'))
# show12 = Show(show_time=format_datetime('2019-05-30 9:15PM'))
# show13 = Show(show_time=format_datetime('2019-06-02 11PM'))
# show14 = Show(show_time=format_datetime('2019-06-16 10PM'))
# show15 = Show(show_time=format_datetime('2019-06-29 8:30PM'))
# show16 = Show(show_time=format_datetime('2019-07-04 10PM'))
# show17 = Show(show_time=format_datetime('2019-07-11 10PM'))

show1 = Show(show_time=format_datetime('2020-02-23 10 PM'))
show2 = Show(show_time=format_datetime('2020-04-21 8 PM'))
show3 = Show(show_time=format_datetime('2020-02-14 7PM'))
show4 = Show(show_time=format_datetime('2020-02-15 7PM'))
show5 = Show(show_time=format_datetime('2020-03-08 9PM'))
show6 = Show(show_time=format_datetime('2020-03-13 9:30PM'))
show7 = Show(show_time=format_datetime('2020-04-22 10:15PM'))
show8 = Show(show_time=format_datetime('2020-04-29 11PM'))
show9 = Show(show_time=format_datetime('2020-05-03 11PM'))
show10 = Show(show_time=format_datetime('2020-05-10 12AM'))
show11 = Show(show_time=format_datetime('2020-05-15 7:45PM'))
show12 = Show(show_time=format_datetime('2020-05-30 9:15PM'))
show13 = Show(show_time=format_datetime('2020-06-02 11PM'))
show14 = Show(show_time=format_datetime('2020-06-16 10PM'))
show15 = Show(show_time=format_datetime('2020-06-29 8:30PM'))
show16 = Show(show_time=format_datetime('2020-07-04 10PM'))
show17 = Show(show_time=format_datetime('2020-07-11 10PM'))

# with db.session.no_autoflush:
#     jezebel.shows = [show3, show4, show12, show13]
#     trash_pit.shows = [show1]
#     skazle.shows = [show2]
#     lit.shows = [show5, show8, show11]
#     bk_life.shows = [show6, show9, show10]
#     nice_traveler.shows = [show14]
#     honkin_tonk.shows = [show15]
#     iron_lung.shows = [show7]
#     rum_drum.shows = [show16, show17]

#     groban.shows = [show1, show2]
#     diablo_bull.shows = [show5, show6]
#     nail_in_coffin.shows = [show7]
#     blake.shows = [show8, show9, show10]
#     ja_mon.shows = [show16, show17]
#     sara_braile.shows = [show3, show14, show15]
#     mature_5.shows = [show4]
#     oos.shows = [show11, show12, show13]

with db.session.no_autoflush:
    shows = [show3, show4, show12, show13]
    for show in shows:
        jezebel.shows.append(show)
    
    trash_pit.shows.append(show1)
    skazle.shows.append(show2)

    shows = [show5, show8, show11]
    for show in shows:
        lit.shows.append(show)

    shows = [show6, show9, show10]
    for show in shows:
        bk_life.shows.append(show)

    nice_traveler.shows.append(show14)
    honkin_tonk.shows.append(show15)
    iron_lung.shows.append(show7)

    shows = [show16, show17]
    for show in shows:
        rum_drum.shows.append(show)

    shows = [show1, show2]
    for show in shows:
        groban.shows.append(show)

    shows = [show5, show6]
    for show in shows:
        diablo_bull.shows.append(show)
    
    nail_in_coffin.shows.append(show7)

    shows = [show8, show9, show10]
    for show in shows:
        blake.shows.append(show)

    shows = [show16, show17]
    for show in shows:
        ja_mon.shows.append(show)

    shows = [show3, show14, show15]
    for show in shows:
        sara_braile.shows.append(show)

    mature_5.shows.append(show4)

    shows = [show11, show12, show13]
    for show in shows:
        oos.shows.append(show) 

try:
    db.session.add(show1)
    db.session.add(show2)
    db.session.add(show3)
    db.session.add(show4)
    db.session.add(show5)
    db.session.add(show6)
    db.session.add(show7)
    db.session.add(show8)
    db.session.add(show9)
    db.session.add(show10)
    db.session.add(show11)
    db.session.add(show12)
    db.session.add(show13)
    db.session.add(show14)
    db.session.add(show15)
    db.session.add(show16)
    db.session.add(show17)
    db.session.commit()
except:
    db.session.rollback()
    print(sys.exc_info())
    
finally:
    db.session.close()
