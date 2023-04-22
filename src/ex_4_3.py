""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_events = get_shutdown_events(logfile)
    
    shutdown_events1 = shutdown_events[0]
    
    shutdown_events2 = shutdown_events[-1]
       
    event1_time = logstamp_to_datetime(shutdown_events1.split()[1])
    
    event2_time = logstamp_to_datetime(shutdown_events2.split()[1])
    
    
    return (event2_time-event1_time)


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
