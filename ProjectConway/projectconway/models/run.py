import datetime
import transaction
from projectconway.lib.exceptions import RunSlotTakenError
from projectconway.models import Base, DBSession
from sqlalchemy import Column, DateTime, Integer, Sequence, String, and_, exc


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
    def get_time_slots_for_hour(cls, time_slot):
        """
        Returns the times slots for the same year, month, day, hour as a
        given datetime object
        """

        min_hour = hourify(time_slot)
        max_hour = hourify(time_slot) + datetime.timedelta(hours=1)
        now = datetime.datetime.now()

        cls._validate_time_slot(now, time_slot)

        # Query the runs that are happening at this hour
        run_times = DBSession.query(Run.time_slot).filter(and_(
            Run.time_slot < max_hour,
            Run.time_slot >= min_hour,
        )).all()
        # Sqlalchemy returns a weird list of tuples
        run_times = [time[0] for time in run_times]

        slots = []
        for slot in range(0, 60, 5):
            t_slot = time_slot.replace(minute=slot, second=0, microsecond=0)
            if now < t_slot and (t_slot not in run_times):
                slots.append(format(slot, "02d"))

        return slots

    @classmethod
    def get_run_for_time_slot(cls, time_slot):
        """
        Returns a run if it exists for the given timeslot otherwise
        return None
        """
        return DBSession.query(Run).filter(Run.time_slot == time_slot).all()

    @classmethod
    def insert_run(cls, pattern, time_slot):
        """
        Ensures that the pattern and time_slot meet validation
        and inserts the run into the run table.
        """
        now = datetime.datetime.now()

        # Perform validation checks
        cls._validate_time_slot(now, time_slot)
        if cls.get_run_for_time_slot(time_slot):
            raise RunSlotTakenError("Time slots already has a run associated")

        # Insert pattern and time slot into database
        with transaction.manager:
            DBSession.add(Run(pattern, time_slot, ""))
            DBSession.commit()

    @classmethod
    def _validate_time_slot(cls, now, time_slot):
        # TODO: Use the values from the project conway init file
        min_date = hourify(now)
        max_date = datetime.datetime.now() + datetime.timedelta(weeks=12)
        max_date = hourify(max_date)

        # Ensure time_slot meets conditions
        if time_slot < min_date:
            raise exc.ArgumentError("Time passed in is in the past")
        elif time_slot > max_date:
            raise exc.ArgumentError("Time is above the maximum")
        if time_slot.minute % 5 != 0:
            raise exc.ArgumentError("Minute value is not a multiple of 5")

def hourify(t):
    return t.replace(minute=0, second=0, microsecond=0)
