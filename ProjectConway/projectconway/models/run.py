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
    def get_runs_for_day(cls, date):
        """
        Returns every run set to take place on a specified date.
        """
        now = datetime.datetime.now()
        start = date
        end = date + datetime.timedelta(days=1)

        # Query the runs that are happening at this hour
        run_times = DBSession.query(Run).filter(and_(
            Run.time_slot < end,
            Run.time_slot >= start,
            Run.time_slot > now,
        )).all()

        return run_times

    @classmethod
    def get_time_slots_for_day(cls, date, now,
                               min_time=project_config["starting_time"], max_time=project_config["closing_time"]):
        """
        Returns all available time slots for the specified date as a
        Date object.
        """

        run_times_for_date = Run.get_runs_for_day(date)
        run_times_for_date = [run.time_slot for run in run_times_for_date]
        slots = []

        for h in range(min_time.hour, max_time.hour + 1):
            if h == max_time.hour and max_time.minute == 0:
                break

            min_min = 0
            max_min = 60
            if h == min_time.hour:
                min_min = min_time.minute
            elif h == max_time.hour:
                max_min = max_time.minute

            for slot in range(min_min, max_min, 5):
                t_slot = datetime.datetime.combine(date, datetime.time(hour=h, minute=slot))
                if t_slot not in run_times_for_date and t_slot > (now + project_config["scheduling_gap"]):
                    slots.append(t_slot)

        return slots

    @classmethod
    def get_run_for_time_slot(cls, time_slot):
        """
        Returns a run if it exists for the given time slot otherwise
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
        if project_config["start_date"]:
            start = datetime.datetime.combine(project_config["start_date"], datetime.time())
        else:
            start = now

        end = None
        if project_config["date_range"]:
            end = start + project_config["date_range"]

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
