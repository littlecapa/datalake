import os
import re

import logging.config
import logging
logger = logging.getLogger("root")
logging.basicConfig(level=logging.DEBUG)

class PGN_Splitter():

    def __init__(self, input_dir, input_file_name, output_subdir, max_lines, offset = 0):
        self.input_dir = input_dir
        self.input_file = os.path.join(input_dir, input_file_name)
        self.output_dir = os.path.join(input_dir, output_subdir)
        self.output_file_name_pattern = os.path.join(self.output_dir, input_file_name)
        self.max_lines = max_lines
        self.offset = offset
    
    def open_next_output_file(self, number):
        file_name = self.output_file_name_pattern.replace(".", "_" + str(number) + ".")
        return open(file_name, "w")

    def is_line_header(self, line):
        # Start with [, End with]
        pattern = r"^\[.*\]$"
        matches = re.findall(pattern, line)
        if matches:
            return True
        else:
            return False

    def split(self):
        if self.max_lines > self.offset:
            next_segment = 0
        else:
            next_segment = round(self.offset/self.max_lines)
        file_out = self.open_next_output_file(next_segment)

        with open(self.input_file, 'r') as file_in:
            index = 0
            total_index = 0
            next_no_header = False
            next_header = False
            for line in file_in:
                total_index += 1
                if self.offset > 0:
                    if self.offset%self.max_lines == 0:
                        logger.debug(f"Current Offset: {self.offset}")

                    self.offset -= 1
                    if self.offset == 0:
                        logger.debug(f"Offset abgearbeitet, start mit {next_segment}")
                    continue
                index += 1
                if index > self.max_lines:
                    logger.debug(f"Limit erreicht:  {index}, Line: {line}, Line number: {total_index}")
                    if next_no_header == False:
                        next_no_header = True
                        #logger.debug(f"Suche nächsten No Header, {index}")
                    elif next_no_header == True and next_header == False:
                        if self.is_line_header(line) == False:
                            next_header = True
                            #logger.debug(f"Suche nächsten Header, {index}")
                    elif next_no_header == True and next_header == True:
                        if self.is_line_header(line) == True:
                            logger.debug(f"Header gefunden, {index}")
                            # Erster Header nach  einem No Header, daher neues File
                            file_out.close()
                            logger.debug(f"File closed, {next_segment}, Line number: {total_index}")
                            next_segment += 1
                            file_out = self.open_next_output_file(next_segment)
                            index = 0
                            next_header = False
                            next_no_header = False
                file_out.write(line)
            file_out.close()
            file_in.close()
                            
