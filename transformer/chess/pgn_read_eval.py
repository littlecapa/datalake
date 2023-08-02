import logging
import re
logger = logging.getLogger("root")
logging.basicConfig(level=logging.DEBUG)

import torch

class Eval_Reader():

    def __init__(self, input_file, seperator = ";"):
        self.input_file = input_file
        self.pattern = r'\[([\d\s-]+)\];([\d.-]+)' + seperator
                
    def read(self):
        try:
            data = []
            labels = []
            index = 0
            logger.debug(f"Input File: {self.input_file}")
            with open(self.input_file) as input:
                # Read each line
                lines = input.readlines()

                # Iterate over each line
                for line in lines:
                    logger.debug(f"{index} Line: {line}")
                    # Extract the numerical values and label using regular expressions
                    match = re.search(self.pattern, line)
                    # Check if a match was found
                    if match:
                        logger.debug(f"Match")
                        # Extract the numerical values and convert them to a PyTorch tensor
                        values = torch.tensor(list(map(int, match.group(1).split())), dtype=torch.float32)
            
                        # Extract the label
                        label = float(match.group(2))
            
                        # Append the values and label to the data list
                        data.append(values)
                        labels.append(label)
                    if index > 100:
                        break
                    else:
                        index +=1
                
        except Exception as e:
            logger.error(str(e))
        finally:
            # Close the PGN files
            input.close()
            logger.debug("All Files closed")

            data = torch.stack(data)
            labels = torch.tensor(labels, dtype=torch.float32)

            return data, labels
        

    