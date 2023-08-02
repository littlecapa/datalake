import sys
sys.path.append('..')

import logging.config
import logging

from bb_filter_kkrr import BB_Filter_KKRR as bbf

def setup_logging():
    logging.basicConfig(
        filename='app.log',  # Change this to your desired log file path
        level=logging.INFO,  # Change the log level as needed (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main():
    setup_logging()
    logging.info('Starting the program')
    for i in range(100,101):
        #new_filter = bbf("/Volumes/Data/DataLake/chess/filtered/eval_mate/commentated_li_"+str(i)+".csv", "/Volumes/Data/DataLake/chess/filtered/eval_mate/kkrr", max_games = 1000000)
        new_filter = bbf("/Volumes/Data/DataLake/chess/filtered/eval_mate/test_li_"+str(i)+".csv", "/Volumes/Data/DataLake/chess/filtered/eval_mate/kkrr", max_games = 1000000)
        
        new_filter.filter()
    logging.info('Program execution completed')

# Call the main function if the script is executed directly
if __name__ == "__main__":
    main()
