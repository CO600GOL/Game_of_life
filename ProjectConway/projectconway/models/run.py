import datetime
import transaction
from projectconway import project_config
from projectconway.lib.exceptions import RunSlotTakenError, RunSlotInvalidError
from projectconway.models import Base, DBSession
from sqlalchemy import Boolean, Column, DateTime, Integer, Sequence, String, and_


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
    sent = Column(Boolean)

    def __init__(self, input_pattern, time_slot, user_name):
        '''
        Initialises an object to be input into
        the table.
        '''
        self.input_pattern = input_pattern
        self.time_slot = time_slot
        self.user_name = user_name
        self.sent = False

    def __repr__(self):
        '''
        Returns: a representation of the table object.
        '''
        return ("Run<Pattern=%s, Time Slot=%s, User Name=%s, Sent=%s>" % (self.input_pattern, self.time_slot, self.user_name, self.sent))

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
    def get_runs_for_day(cls, date):
        """
        Returns every run set to take place on a specified date.
        """
        pass

    @classmethod
    def get_time_slots_for_day(cls, date):
        """
        Returns all available time slots for the specified date as a
        Date object.
        """
        pass

    @classmethod
    def get_run_for_time_slot(cls, time_slot):
        """
        Returns a run if it exists for the given timeslot otherwise
        return None
        """
        return DBSession.query(Run).filter(Run.time_slot == time_slot).all()

    @classmethod
    def get_unsent_runs(cls, min_time):
        """
        Retrieves all of the currently unsent patterns on the database that are
        set to occur after the minimum time.
        """
        with transaction.manager:
            unsent_runs = DBSession.query(Run).filter(and_(
                Run.time_slot > min_time,
                Run.sent == False
            )).all()

            for run in unsent_runs:
                run.sent = True

            DBSession.commit()

        return unsent_runs

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

        if project_config["start_date"]:
            start = project_config["starting_date"]
        else:
            start = now

        if project_config["date_range"]:
            end = now + project_config["date_range"]

        # Ensure time_slot meets conditions
        if time_slot < start:
            raise RunSlotInvalidError("Time passed in is in the past")
        elif end:
            if time_slot > end:
                raise RunSlotInvalidError("Time is above the maximum")
        if time_slot.minute % 5 != 0:
            raise RunSlotInvalidError("Minute value is not a multiple of 5")

    def json(self):
        """
        Returns a json dictionary representing this object.
        """
        return {
            "id": self.id,
            "input_pattern": self.input_pattern.replace("\n", "\\n"),
            "time_slot": self.time_slot.isoformat(),
            "sent": self.sent
        }


def hourify(t):
    return t.replace(minute=0, second=0, microsecond=0)
