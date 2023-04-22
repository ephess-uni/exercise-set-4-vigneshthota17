""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    with open(logfile, 'r') as logfile_read:
        
        reads = logfile_read.read()
    
    allreads = reads.splitlines()
    
    shutdown_events = list()
    
    for read in allreads:
        
        if 'Shutdown initiated' in read :
            
            shutdown_events.append(read)
        
    
    return shutdown_events


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
