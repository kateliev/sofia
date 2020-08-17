# MODULE: SOFIA / LIB / IO
# NOTE: Assorted IO Tools
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2020 		(http://www.kateliev.com)
#------------------------------------------------------------
# https://kateliev.github.io/sofia/

# No warranties. By using this you agree
# that you use it at your own risk!

from __future__ import unicode_literals, print_function
import json, json.scanner

from objects import attribdict

# - Init -------------------------------
__version__ = '0.0.2'

# - IO Parsers -------------------------
class io_json_decoder(json.JSONDecoder):
	def __init__(self, *args, **kwdargs):
		super(io_json_decoder, self).__init__(*args, **kwdargs)
		self.__parse_object = self.parse_object
		self.parse_object = self._parse_object
		self.scan_once = json.scanner.py_make_scanner(self)
		self.__tree_class = attribdict
	
	def _parse_object(self, *args, **kwdargs):
		result = self.__parse_object(*args, **kwdargs)
		tree_obj = self.__tree_class(result[0])
		tree_obj.lock() # Lock the tree - no further editing allowed
		return tree_obj, result[1]

class io_json_encoder(json.JSONEncoder):
	def __init__(self, *args, **kwdargs):
		super(io_json_encoder, self).__init__(*args, **kwdargs)
	
	def default(self, obj):
		return super(vfj_encoder, self).default(obj)