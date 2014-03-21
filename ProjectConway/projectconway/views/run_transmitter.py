"""
This module contains logic for transmitting display runs that have not yet been sent to the Raspberry Pi from the
server-side database.
"""

from datetime import datetime
from projectconway.models.run import Run
from pyramid.view import view_config

@view_config(route_name='run_transmitter', renderer='conway_json')
def run_transmitter_view(request):
    """
    This function executes the transmission of unsent server patterns to the display.

    @param request The request sent to this page of the web application.
    """

    #TODO: Write authentication logic! Quickly!
    # ...
    #TODO: Look into official authentication logic

    min_time = request.POST["min_time"]
    min_time = datetime.strptime(min_time, "%Y-%m-%dT%H:%M:%S.%f")

    unsent_runs = Run.get_unsent_runs(min_time)
    unsent_runs = [run.json() for run in unsent_runs]

    return unsent_runs