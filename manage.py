#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from subprocess import Popen, PIPE
import sys


def main():
    imageUpload()
    os.chdir(r"C:\Users\Lenovo\Desktop\Documents\GitHub\DocRoc")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def imageUpload():
    os.chdir(r"C:\Users\Lenovo\Desktop\Documents\GitHub\DocRoc\WeeklyUpdate")
    p = Popen(['python', 'main.py'], stdin=PIPE, bufsize=0)
    return ('')

if __name__ == '__main__':
    main()
  
