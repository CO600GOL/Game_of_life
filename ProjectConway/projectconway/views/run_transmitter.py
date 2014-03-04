"""
This view is responsible for the logic that trasmits currently unsent patterns on the server
to the raspberry pi controlloing the display.
"""

from datetime import datetime
from projectconway.models.run import Run
from pyramid.view import view_config

@view_config(route_name='run_transmitter', renderer='json')
def run_transmitter_view(request):
    """
    Executes the transmission of unsent server patterns to the display.
    """

    #TODO: Write authentication logic! Quickly!
    # ...
    #TODO: Look into official authetication logic

    min_time = request.POST["min_time"]
    min_time = datetime.strptime(min_time, "%Y-%m-%dT%H:%M:%S.%f")

    unsent_runs = Run.get_unsent_runs(min_time)
    unsent_runs = [run.json() for run in unsent_runs]

    return unsent_runs