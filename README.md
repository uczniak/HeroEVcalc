# HeroEVcalc
Script calculating $EV for HERO SNGs on partypoker (by connecting to PT4/HM2 database).

Assumes PostgreSQL user is 'postgres', prompts for password and DB name.
Proceeds to prompt for player name(s) and start/end dates (optional).

Prints out per player summary with number of tournaments, number of hands, hands/tourney, cev/tourney, cev/hand, number of bounties, bounty %, total $EV, EV ROI, $EV/tourney, total rake.
Proceeds to ask for RB % to provide post-RB figures. Shows graph of real $ vs $EV.

Depends on PT4 import and works by comparing amount won vs prizepool, so any import errors might distort result. HM2 version uses HM API and needs HM2 open and Hero set as active player.

Requires: peewee, matplotlib and their dependencies, in particular psycopg2, tkinter. HM2 uses requests as well (for API).
