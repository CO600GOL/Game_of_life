import datetime
from projectconway.models import Base, DBSession
from sqlalchemy import Column, DateTime, Index, Integer, Sequence, String, and_, extract


class Run(Base):
    '''
    This class contains the logic necessary for the database to hold
    an instance of the Run table, in which a single run of the
    Game Of Life will be held.
    '''
    __tablename__ = "runs"

    id = Column(Integer, Sequence('run_id_seq'), primary_key=True)
    input_pattern = Column(String)
    time_slot = Column(DateTime)
    user_name = Column(String(50))

    def __init__(self, input_pattern, time_slot, user_name):
        '''
        Initialises an object to be input into
        the table.
        '''
        self.input_pattern = input_pattern
        self.time_slot = time_slot
        self.user_name = user_name

    def __repr__(self):
        '''
        Returns: a representation of the table object.
        '''
        return ("Run<Pattern=%s, Time Slot=%s, User Name=%s>" % (self.input_pattern, self.time_slot, self.user_name))

    @classmethod
    def get_time_slots_match_hour(cls, time_slot):
        """
        Returns the times slots for the same year, month, day, hour as a
        given datetime object
        """
        min_hour = time_slot.replace(minute=0, second=0, microsecond=0)
        max_hour = time_slot.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1)

        return DBSession.query(Run.time_slot).filter(and_(
            Run.time_slot <= max_hour,
            Run.time_slot >= min_hour
        )).all()
