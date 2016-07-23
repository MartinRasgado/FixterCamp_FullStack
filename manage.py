#!/usr/bin/env python
#comentario8
#comentario7
#comentario6
#comentario5
#comentario4
#comentando3
#comentando2
#comentaalgo
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "holamundo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
