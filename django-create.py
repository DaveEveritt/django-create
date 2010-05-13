#!/usr/bin/env python

"""Creates a new Django project in a specified location.

Place this script somewhere handy and run with: python django_start.py
Either add the path to your Django projects to the 'project_dir' 
variable, or leave blank for a prompt to your Django project location.
"""

import os

project_dir = "/Users/deveritt/djangocode"

"""Creates new Django project only if user has entered 'y'."""
def make_project(*args):
	if args[0] == 'y':
		os.chdir(args[1])
		print "\nCreating project in '%s'." % os.getcwd()
		os.system("django-admin.py startproject %s" % args[2])
		print "\nNew files in your new project directory '%s':" % args[2]
		os.chdir(args[2])
		os.system("ls -al")
		print "\nGo to project:\ncd %s" % os.path.join (args[1], args[2])
	else:
		print "No Django project created."

if project_dir == '':
	project_dir = raw_input("Enter path to your Django project code: ")

project = raw_input("Name your Django project: ")

"""Presents choice to proceed if path exists, or shows bad path."""
if os.path.isdir(project_dir)==1:
	goahead = raw_input("\nCreate Django project '%s' in: %s?"\
						"\n('y' or 'n'): " % (project, project_dir))
	make_project(goahead, project_dir, project)
else:
	print "Can't use path: '%s'." % project_dir
