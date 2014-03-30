"""
This module contains the logic for initialising and running the server-side database. This database must hold users'
patterns and the datetime at which the user wants it to be run.
"""

import datetime
import transaction
from projectconway import project_config
from projectconway.lib.exceptions import RunSlotTakenError, RunSlotInvalidError
from projectconway.models import Base, DBSession
from sqlalchemy import Boolean, Column, DateTime, Integer, Sequence, String, and_


class Run(Base):
    """
    This class represents the runs table within the server-side database, in which a single user's pattern and the
    datetime at which they want it to run is held in a table row.
    """
    __tablename__ = "runs"

    # The unique identifier of a run.
    id = Column(Integer, Sequence('run_id_seq'), primary_key=True)
    # The user's pattern.
    input_pattern = Column(String)
    # The datetime at which the user wants their pattern to be run.
    time_slot = Column(DateTime)
    user_name = Column(String(50))
    # A boolean value saying whether or not a run has been sent to the Raspberry Pi.
    sent = Column(Boolean)

    def __init__(self, input_pattern, time_slot, user_name):
        """
        Initialises an object to be input into
        the table.

        Ctor - Initialises a row of the database.

        @param input_pattern The pattern to be stored in the table.
        @param time_slot The datetime at which the pattern should be run.
        """
        self.input_pattern = input_pattern
        self.time_slot = time_slot
        self.user_name = user_name
        self.sent = False

    def __repr__(self):
        """
        This method retrieves a string representing a single row of the table.

        @return The string representation of the table row.
        """
        return ("Run<Pattern=%s, Time Slot=%s, User Name=%s, Sent=%s>" % (self.input_pattern, self.time_slot,
                                                                          self.user_name, self.sent))

    @classmethod
    def get_runs_for_day(cls, date):
        """
        This method retrieves every run set to take place on the given data.

        @param date The date for which the runs to take place should be retrieved.

        @return The runs set to take place for the day.
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

        This method retrieves all the available time slots for the specified date.

        @param date The date for which all the available time slots should be retrieved.

        @return The available time slots for the day.
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
        @param time_slot The time slot the database should query for a run.

        @return The run that occupies the specified time slot if one exists, otherwise None.

        Returns a run if it exists for the given time slot otherwise
        return None
        """
        return DBSession.query(Run).filter(Run.time_slot == time_slot).all()

    @classmethod
    def get_unsent_runs(cls, min_time):
        """
        This method retrieves all of the currently unsent patterns in the database that are set to occur after the
        given minimum time.

        @param min_time The time after which the database should be query.

        @return unsent_runs The runs that have not yet been sent to the Raspberry Pi.
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

        This method ensures that the pattern and time slot meet validation before inserting the run into the runs table
        of the server-side database.

        @param pattern The pattern to input into the table.
        @param time_slot The datetime at which the pattern should be run.
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
        """
        This method ensures the time slot being checked is valid.

        @param now The current date and time
        @param time_slot The time slot to validate.
        """
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
        This method creates a JSON dictionary representing the table row.

        @return The JSON dictionary.
        """
        return {
            "id": self.id,
            "input_pattern": self.input_pattern.replace("\n", "\\n"),
            "time_slot": self.time_slot.isoformat(),
            "sent": self.sent
        }


def hourify(t):
    """
    This function makes the given time accurate to the hour.

    @return The hour-accurate time.
    """
    return t.replace(minute=0, second=0, microsecond=0)
