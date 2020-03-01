import sys
import os
import logging
import datetime
import traceback
import random
import string

import program.library.helpers as helpers

helpers.installRequirements()

from program.library.helpers import get
from program.library.gmail import Gmail

class Main:
    def run(self):
        logging.info('Starting')

        inputRows = self.options['emailsToExport']

        try:
            self.gmail.export(inputRows)
        except Exception as e:
            helpers.handleException(e)
        
        self.cleanUp()

    def cleanUp(self):
        logging.info('Done')

    def __init__(self):
        helpers.setUpLogging('user-data/logs')

        # set default options
        self.options = {
            'outputFile': 'user-data/output/output.csv',
            'emailsToExport': '',
            'readOnly': 1,
            'resourceUrl': 'program/resources/resource'
        }

        optionsFileName = helpers.getParameter('--optionsFile', False, 'user-data/options.ini')
        
        # read the options file
        helpers.setOptions(optionsFileName, self.options)

        self.gmail = Gmail(self.options)

if __name__ == '__main__':
    main = Main()
    main.run()