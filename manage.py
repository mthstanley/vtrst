#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv, find_dotenv

# load enviroment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'vtrst/settings/.env')
load_dotenv(dotenv_path)

if __name__ == "__main__":

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
