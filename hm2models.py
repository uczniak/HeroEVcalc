from peewee import *
from playhouse.postgres_ext import *
from database_management import database

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Aliases(BaseModel):
    aliasplayer = IntegerField(db_column='aliasplayer_id', null=True)
    player = IntegerField(db_column='player_id', null=True)

    class Meta:
        db_table = 'aliases'

class Bonuses(BaseModel):
    bonus = PrimaryKeyField(db_column='bonus_id')
    bonusamountincents = IntegerField()
    bonustimestamp = DateTimeField(null=True)
    currencytype = IntegerField(db_column='currencytype_id', null=True)
    description = CharField(null=True)
    player = IntegerField(db_column='player_id')

    class Meta:
        db_table = 'bonuses'

class Compiledplayerresults(BaseModel):
    bbgroup = IntegerField(db_column='bbgroup_id')
    bigblindstealattempted = IntegerField()
    bigblindstealdefended = IntegerField()
    bigblindstealreraised = IntegerField()
    calledflopcontinuationbet = IntegerField()
    calledfourbetpreflop = IntegerField()
    calledrivercontinuationbet = IntegerField()
    calledthreebetpreflop = IntegerField()
    calledturncontinuationbet = IntegerField()
    calledtwopreflopraisers = IntegerField()
    compiledplayerresults = PrimaryKeyField(db_column='compiledplayerresults_id')
    couldcoldcall = IntegerField()
    couldsqueeze = IntegerField()
    couldthreebet = IntegerField()
    didcoldcall = IntegerField()
    didsqueeze = IntegerField()
    didthreebet = IntegerField()
    facedfourbetpreflop = IntegerField()
    facedthreebetpreflop = IntegerField()
    facingflopcontinuationbet = IntegerField()
    facingrivercontinuationbet = IntegerField()
    facingturncontinuationbet = IntegerField()
    facingtwopreflopraisers = IntegerField()
    flopcontinuationbetmade = IntegerField()
    flopcontinuationbetpossible = IntegerField()
    foldedtoflopcontinuationbet = IntegerField()
    foldedtofourbetpreflop = IntegerField()
    foldedtorivercontinuationbet = IntegerField()
    foldedtothreebetpreflop = IntegerField()
    foldedtoturncontinuationbet = IntegerField()
    gametype = IntegerField(db_column='gametype_id')
    numberofplayers = IntegerField()
    pfrhands = IntegerField()
    playedyearandmonth = IntegerField()
    player = IntegerField(db_column='player_id')
    raisedflopcontinuationbet = IntegerField()
    raisedfourbetpreflop = IntegerField()
    raisedrivercontinuationbet = IntegerField()
    raisedthreebetpreflop = IntegerField()
    raisedturncontinuationbet = IntegerField()
    raisedtwopreflopraisers = IntegerField()
    rivercallippassonturncb = IntegerField()
    rivercontinuationbetmade = IntegerField()
    rivercontinuationbetpossible = IntegerField()
    riverfoldippassonturncb = IntegerField()
    riverraiseippassonturncb = IntegerField()
    sawflop = IntegerField()
    sawlargeshowdown = IntegerField()
    sawlargeshowdownlimpedflop = IntegerField()
    sawnonsmallshowdown = IntegerField()
    sawnonsmallshowdownlimpedflop = IntegerField()
    sawshowdown = IntegerField()
    smallblindstealattempted = IntegerField()
    smallblindstealdefended = IntegerField()
    smallblindstealreraised = IntegerField()
    totalaggressivepostflopstreetsseen = IntegerField()
    totalamountwonincents = IntegerField()
    totalbbswon = IntegerField()
    totalbets = IntegerField()
    totalcalls = IntegerField()
    totalhands = IntegerField()
    totalpostflopstreetsseen = IntegerField()
    totalrakeincents = IntegerField()
    turncallippassonflopcb = IntegerField()
    turncontinuationbetmade = IntegerField()
    turncontinuationbetpossible = IntegerField()
    turnfoldippassonflopcb = IntegerField()
    turnraiseippassonflopcb = IntegerField()
    vpiphands = IntegerField()
    wonhand = IntegerField()
    wonhandwhensawflop = IntegerField()
    wonhandwhensawriver = IntegerField()
    wonhandwhensawturn = IntegerField()
    wonlargeshowdown = IntegerField()
    wonlargeshowdownlimpedflop = IntegerField()
    wonnonsmallshowdown = IntegerField()
    wonnonsmallshowdownlimpedflop = IntegerField()
    wonshowdown = IntegerField()

    class Meta:
        db_table = 'compiledplayerresults'
        indexes = (
            (('playedyearandmonth', 'numberofplayers', 'gametype', 'bbgroup'), False),
            (('player', 'playedyearandmonth', 'numberofplayers', 'gametype', 'bbgroup'), False),
        )

class ErrorHands(BaseModel):
    error_hands = PrimaryKeyField(db_column='error_hands_id')
    filename = TextField(null=True)
    gamenumber = BigIntegerField()
    handhistory = TextField()
    pokersite = IntegerField(db_column='pokersite_id')

    class Meta:
        db_table = 'error_hands'
        indexes = (
            (('gamenumber', 'pokersite'), False),
        )

class Gametypes(BaseModel):
    anteincents = IntegerField()
    bigblindincents = IntegerField()
    currencytype = IntegerField(db_column='currencytype_id')
    gametype = PrimaryKeyField(db_column='gametype_id')
    istourney = BooleanField()
    pokergametype = IntegerField(db_column='pokergametype_id')
    smallblindincents = IntegerField()
    tablesize = IntegerField()

    class Meta:
        db_table = 'gametypes'

class Handmarkcategories(BaseModel):
    category = PrimaryKeyField(db_column='category_id')
    color_index = IntegerField(null=True)
    description = TextField(null=True)

    class Meta:
        db_table = 'handmarkcategories'

class HandMarkings(BaseModel):
    gamenumber = BigIntegerField(null=True)
    marking = ForeignKeyField(db_column='marking_id', null=True, rel_model=Handmarkcategories, to_field='category')
    site = IntegerField(db_column='site_id', null=True)

    class Meta:
        db_table = 'hand_markings'

class HandNotes(BaseModel):
    category = IntegerField(db_column='category_id', null=True)
    display_order = IntegerField(null=True)
    gamenumber = BigIntegerField()
    hand_note = PrimaryKeyField(db_column='hand_note_id')
    icon = IntegerField(db_column='icon_id', null=True)
    note = TextField(null=True)
    pokersite = IntegerField(db_column='pokersite_id')

    class Meta:
        db_table = 'hand_notes'

class Handhistories(BaseModel):
    filename = TextField(null=True)
    gamenumber = BigIntegerField()
    gametype = IntegerField(db_column='gametype_id', null=True)
    handhistory = TextField()
    handhistory_id = PrimaryKeyField()
    handtimestamp = DateTimeField(null=True)
    pokersite = IntegerField(db_column='pokersite_id')
    tourneynumber = CharField(null=True)

    class Meta:
        db_table = 'handhistories'
        indexes = (
            (('gamenumber', 'pokersite'), False),
            (('handtimestamp', 'gametype'), False),
            (('handtimestamp', 'gametype'), False),
        )

class HandhistoriesSync(BaseModel):
    handhistories = ForeignKeyField(db_column='handhistories_id', rel_model=Handhistories, to_field='handhistory_id')
    handhistories_sync = PrimaryKeyField(db_column='handhistories_sync_id')
    islocal = BooleanField()
    sync_batch = IntegerField(db_column='sync_batch_id')

    class Meta:
        db_table = 'handhistories_sync'
        indexes = (
            (('handhistories', 'sync_batch'), False),
        )

class Importedfiles(BaseModel):
    filename = TextField(index=True)
    filesize = IntegerField(null=True)
    importedfile = PrimaryKeyField(db_column='importedfile_id')
    lastimportedhandnumber = BigIntegerField(null=True)
    lastmodifieddate = DateTimeField()

    class Meta:
        db_table = 'importedfiles'

class Importsummaries(BaseModel):
    filesprocessed = IntegerField()
    handsper100seconds = IntegerField()
    handsprocessed = IntegerField()
    importsummaries = PrimaryKeyField(db_column='importsummaries_id')
    source = IntegerField()
    timestamp = DateTimeField()

    class Meta:
        db_table = 'importsummaries'
        indexes = (
            (('timestamp', 'source'), False),
        )

class Importsummarydetails(BaseModel):
    errortype = IntegerField()
    filename = TextField(null=True)
    handhistory = TextField(null=True)
    importsummaries = IntegerField(db_column='importsummaries_id')
    importsummarydetails = PrimaryKeyField(db_column='importsummarydetails_id')

    class Meta:
        db_table = 'importsummarydetails'

class NoteCategories(BaseModel):
    category = PrimaryKeyField(db_column='category_id')
    description = TextField()
    display_order = IntegerField()
    use_for_hands = BooleanField()
    use_for_players = BooleanField()

    class Meta:
        db_table = 'note_categories'

class NotecaddyData(BaseModel):
    data = TextField(null=True)
    player = PrimaryKeyField(db_column='player_id')
    user = IntegerField(db_column='user_id', null=True)

    class Meta:
        db_table = 'notecaddy_data'

class NotecaddyDefinitions(BaseModel):
    definition = TextField(db_column='definition_id', primary_key=True)
    note = IntegerField(db_column='note_id', null=True)

    class Meta:
        db_table = 'notecaddy_definitions'

class NotecaddyMetrics(BaseModel):
    data = TextField(null=True)

    class Meta:
        db_table = 'notecaddy_metrics'

class NotecaddyScatter(BaseModel):
    data = TextField(null=True)
    player = PrimaryKeyField(db_column='player_id')

    class Meta:
        db_table = 'notecaddy_scatter'

class NotecaddyTiming(BaseModel):
    actions = UnknownField(null=True)  # ARRAY
    handid = IntegerField()
    playerid = IntegerField()
    streets = UnknownField(null=True)  # ARRAY
    strengths = UnknownField(null=True)  # ARRAY
    timings = UnknownField(null=True)  # ARRAY

    class Meta:
        db_table = 'notecaddy_timing'
        indexes = (
            (('playerid', 'handid'), True),
        )
        primary_key = CompositeKey('handid', 'playerid')

class Players(BaseModel):
    cashhands = IntegerField()
    icon = IntegerField(null=True)
    optimizationstatus = IntegerField()
    player = PrimaryKeyField(db_column='player_id')
    playername = TextField()
    pokersite = IntegerField(db_column='pokersite_id')
    tourneyhands = IntegerField()

    class Meta:
        db_table = 'players'
        indexes = (
            (('playername', 'pokersite'), False),
        )

class PlayerNotes(BaseModel):
    category = ForeignKeyField(db_column='category_id', null=True, rel_model=NoteCategories, to_field='category')
    date_created = DateTimeField(null=True)
    display_order = IntegerField(null=True)
    gamenumber = BigIntegerField(null=True)
    icon = IntegerField(db_column='icon_id', null=True)
    note = TextField(null=True)
    player = ForeignKeyField(db_column='player_id', null=True, rel_model=Players, to_field='player')
    player_note = PrimaryKeyField(db_column='player_note_id')
    pokersite = IntegerField(db_column='pokersite_id', null=True)

    class Meta:
        db_table = 'player_notes'

class Pokerhands(BaseModel):
    gamenumber = BigIntegerField(index=True)
    pokerhand = PrimaryKeyField(db_column='pokerhand_id')
    pokersite = IntegerField(db_column='pokersite_id')

    class Meta:
        db_table = 'pokerhands'

class Pokertables(BaseModel):
    pokertable = PrimaryKeyField(db_column='pokertable_id')
    tablename = CharField()

    class Meta:
        db_table = 'pokertables'

class Rakeback(BaseModel):
    description = CharField(null=True)
    player = IntegerField(db_column='player_id')
    rakeback_endtimestamp = DateTimeField(null=True)
    rakeback = PrimaryKeyField(db_column='rakeback_id')
    rakeback_pct = FloatField()
    rakeback_starttimestamp = DateTimeField(null=True)

    class Meta:
        db_table = 'rakeback'

class Readsettings(BaseModel):
    databaseversion = TextField(null=True)
    lastid = BigIntegerField(null=True)
    lastnoteid = IntegerField(null=True)
    lastomahacash = BigIntegerField(null=True)
    lastomahatournament = BigIntegerField(null=True)
    lasttournament = BigIntegerField(null=True)

    class Meta:
        db_table = 'readsettings'

class Schemainfo(BaseModel):
    version = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'schemainfo'

class Settings(BaseModel):
    key = CharField(primary_key=True)
    value = CharField(null=True)

    class Meta:
        db_table = 'settings'

class SwQuizHandRanges(BaseModel):
    handrange = TextField(null=True)
    path = TextField(null=True)
    quiz_hand = IntegerField(db_column='quiz_hand_id', index=True)
    quiz_hand_range = PrimaryKeyField(db_column='quiz_hand_range_id')

    class Meta:
        db_table = 'sw_quiz_hand_ranges'

class SwQuizHands(BaseModel):
    blinds = CharField(null=True)
    correctherohandrank = IntegerField()
    handhistory = TextField(null=True)
    handnumber = IntegerField(null=True)
    heroposition = CharField(null=True)
    playercount = IntegerField(null=True)
    previousaction = CharField(null=True)
    quiz_hand = PrimaryKeyField(db_column='quiz_hand_id')
    quiz = IntegerField(db_column='quiz_id', index=True)
    score = IntegerField()
    timestamp = DateTimeField()
    useranswerherohandrank = IntegerField()

    class Meta:
        db_table = 'sw_quiz_hands'

class SwQuizPlayers(BaseModel):
    actionamount = IntegerField()
    actiontype = IntegerField()
    name = TextField(null=True)
    opponentmodel = TextField()
    quiz_hand = IntegerField(db_column='quiz_hand_id', index=True)
    quiz_player = PrimaryKeyField(db_column='quiz_player_id')
    seat = IntegerField()
    stack = IntegerField()

    class Meta:
        db_table = 'sw_quiz_players'

class SwQuizzes(BaseModel):
    activetablecount = IntegerField()
    defaultopponentmodel = TextField()
    heroaction = IntegerField()
    heroposition = IntegerField()
    maximumblindlevel = IntegerField()
    maximumherostackinbigblinds = IntegerField()
    maximumplayercount = IntegerField()
    minimumblindlevel = IntegerField()
    minimumherostackinbigblinds = IntegerField()
    minimumplayercount = IntegerField()
    opponentpreviousaction = IntegerField()
    opponentreviousactionposition = IntegerField()
    pokersite = IntegerField(db_column='pokersite_id')
    quiz = PrimaryKeyField(db_column='quiz_id')
    stackroundoff = IntegerField()
    timestamp = DateTimeField(index=True)
    tournamenttagname = TextField()

    class Meta:
        db_table = 'sw_quizzes'

class SyncBatches(BaseModel):
    datatype = CharField()
    remote_batch_num = IntegerField()
    site = CharField()
    sync_batches = PrimaryKeyField(db_column='sync_batches_id')

    class Meta:
        db_table = 'sync_batches'
        indexes = (
            (('datatype', 'site', 'remote_batch_num'), False),
        )

class SyncPrefs(BaseModel):
    db = CharField(null=True)
    host = CharField(null=True)
    lastsyncdate = DateTimeField(null=True)
    name = CharField()
    sync_prefs = PrimaryKeyField(db_column='sync_prefs_id')

    class Meta:
        db_table = 'sync_prefs'

class Tooltips(BaseModel):
    category = CharField(index=True, null=True)
    link = CharField(null=True)
    teaser = CharField(null=True)
    title = CharField(null=True)
    tooltipid = PrimaryKeyField()

    class Meta:
        db_table = 'tooltips'

class Tourneydata(BaseModel):
    bountyincents = IntegerField(null=True)
    buyinincents = IntegerField()
    currency = IntegerField(db_column='currency_id')
    filelastmodifiedtime = DateTimeField()
    filename = TextField()
    finishposition = IntegerField()
    firsthandtimestamp = DateTimeField(null=True)
    icmadjustedwinnings = IntegerField()
    importtype = IntegerField(db_column='importtype_id')
    lasthandtimestamp = DateTimeField(null=True)
    player = IntegerField(db_column='player_id')
    pokergametype = IntegerField(db_column='pokergametype_id')
    rakeincents = IntegerField()
    rebuyamountincents = IntegerField()
    site = IntegerField(db_column='site_id')
    speedtype = IntegerField(db_column='speedtype_id')
    startingstacksizeinchips = IntegerField()
    tablesize = IntegerField()
    tourneydata = PrimaryKeyField(db_column='tourneydata_id')
    tourneyendedforplayer = BooleanField()
    tourneynumber = CharField()
    tourneysize = IntegerField()
    tourneytables = IntegerField()
    tourneytagscsv = TextField()
    userassignedtagname = TextField(null=True)
    winningsdescription = TextField()
    winningsincents = IntegerField()

    class Meta:
        db_table = 'tourneydata'
        indexes = (
            (('tourneynumber', 'player'), False),
            (('tourneynumber', 'site'), False),
        )

class Tourneysummaries(BaseModel):
    buyinincents = IntegerField()
    currency = IntegerField(db_column='currency_id')
    handtimestamp = DateTimeField()
    pokergametype = IntegerField(db_column='pokergametype_id')
    pokersite = IntegerField(db_column='pokersite_id')
    rakeincents = IntegerField()
    speedtype = IntegerField(db_column='speedtype_id')
    tourneynumber = CharField()
    tourneysize = IntegerField()
    tourneysummary = PrimaryKeyField(db_column='tourneysummary_id')
    tourneysummarytext = TextField()
    tourneytables = IntegerField()

    class Meta:
        db_table = 'tourneysummaries'
        indexes = (
            (('pokersite', 'tourneynumber'), False),
        )

class Uploadedtosnowie(BaseModel):
    handhistory = ForeignKeyField(db_column='handhistory_id', primary_key=True, rel_model=Handhistories, to_field='handhistory_id')

    class Meta:
        db_table = 'uploadedtosnowie'

