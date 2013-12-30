from projectconway.models import Base
from projectconway.models.run import Run
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence


class TimeSlot(Base):
    '''
    This class containst the logic necessary for the database to hold
    an instance of the Time Slot table, in which a time slot, taken by
    of the user, will be held.
    '''
    __tablename__ = "time slots"
    
    id = Column(Integer, Sequence('time_slot_id_seq'), primary_key=True)
    run_id = Column(Integer, ForeignKey('runs.id'))
    time_slot = Column(DateTime)
    
    def __init__(self, run_id, time_slot):
        '''
        Initialises a single TimeSlot object to be set inside
        the time slot table.
        '''
        self.run_id = run_id
        self.time_slot = time_slot
    
    def __repr__(self):
        '''
        Returns a representation of a time slots table object.
        '''
        return("TimeSlot<%s, %s>" % (self.run_id, self.time_slot))