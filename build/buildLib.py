#buildLib.py

from jinja2 import Template
import re
import json
import os

def writeToFile( _file, _text ):
	f = open( _file, "w" )
	f.write( _text )
	f.close()

def loadTemplate( _temp ):
	f = open( _temp )
	text = f.read()
	f.close()
	return text

def getFilePrefix( _path ):
    # Get the json file path
	dirs = os.path.split( _path )
	f = _path + "/" + dirs[ len( dirs ) - 1 ]
	return f

def jsonFileToPython( _file ):
    # Turn a json file into a python object
	f = open( _file, "r" )
	data = json.load( f )
	f.close();
	return data

def parseTemplate( _template, _file, _data ):
	# Load the template
	tempRaw = loadTemplate( _template )
	
	# Build a jinja template
	template = Template( tempRaw )
	
	# Double asterisk?
	# not necessary in Python 2.6.1
	text = template.render( _data )
	writeToFile( _file, text )

def stripHtml( _data ):
	p = re.compile( r"<.*?>" )
	return p.sub( "", _data )

def htmlToPreview( _html, _n ):
	_html = stripHtml( _html )
	words = _html.split( " " )
	return " ".join( words[:_n] ) + " ..."