# MODULE: SOFIA / LIB / Objects
# NOTE: Assorted objects
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2020 		(http://www.kateliev.com)
#------------------------------------------------------------
# https://kateliev.github.io/sofia/

# No warranties. By using this you agree
# that you use it at your own risk!

# - Dependencies ------------------------
from __future__ import print_function
from collections import MutableSequence, MutableMapping, defaultdict

# - Init -------------------------------
__version__ = '0.0.2'

# - Objects ----------------------------
class CustomDict(MutableMapping):
	'''A more or less complete user-defined wrapper around dictionary objects.
	Adapted from Source: https://github.com/enthought/Python-2.7.3/blob/master/Lib/self.__class__.py
	'''
	def __init__(self, dict=None, **kwargs):
		self.data = {}
		if dict is not None:
			self.update(dict)
			
		if len(kwargs):
			self.update(kwargs)

	def __repr__(self): 
		return repr(self.data)

	def __cmp__(self, dict):
		if isinstance(dict, self.__class__):
			return cmp(self.data, dict.data)
		else:
			return cmp(self.data, dict)

	__hash__ = None

	def __len__(self): 
		return len(self.data)

	def __getitem__(self, key):
		if key in self.data:
			return self.data[key]
		if hasattr(self.__class__, "__missing__"):
			return self.__class__.__missing__(self, key)
		raise KeyError(key)

	def __setitem__(self, key, item): 
		self.data[key] = item

	def __delitem__(self, key): 
		del self.data[key]

	def __iter__(self):
		return iter(self.data)

	def clear(self): 
		self.data.clear()

	def copy(self):
		if self.__class__ is self.__class__:
			return self.__class__(self.data.copy())
		import copy
		data = self.data
		try:
			self.data = {}
			c = copy.copy(self)
		finally:
			self.data = data
		c.update(self)
		return c

	def keys(self): 
		return self.data.keys()

	def items(self): 
		return self.data.items()

	def iteritems(self): 
		return self.data.iteritems()

	def iterkeys(self): 
		return self.data.iterkeys()

	def itervalues(self): 
		return self.data.itervalues()

	def values(self): 
		return self.data.values()

	def has_key(self, key): 
		return key in self.data

	def update(self, dict=None, **kwargs):
		if dict is None:
			pass
		elif isinstance(dict, self.__class__):
			self.data.update(dict.data)
		elif isinstance(dict, type({})) or not hasattr(dict, 'items'):
			self.data.update(dict)
		else:
			for k, v in dict.items():
				self[k] = v
		if len(kwargs):
			self.data.update(kwargs)

	def get(self, key, failobj=None):
		if key not in self:
			return failobj
		return self[key]

	def setdefault(self, key, failobj=None):
		if key not in self:
			self[key] = failobj
		return self[key]

	def pop(self, key, *args):
		return self.data.pop(key, *args)

	def popitem(self):
		return self.data.popitem()

	def __contains__(self, key):
		return key in self.data

	@classmethod
	def fromkeys(cls, iterable, value=None):
		d = cls()
		for key in iterable:
			d[key] = value
		return d


class attribdict(defaultdict):
	'''Default dictionary where keys can be accessed as attributes.'''
	def __init__(self, *args, **kwdargs):
		super(attribdict, self).__init__(attribdict, *args, **kwdargs)

	def __getattribute__(self, name):
		try:
			return object.__getattribute__(self, name)
		except AttributeError:
			try:
				return self[name]
			except KeyError:
				raise AttributeError(name)
		
	def __setattr__(self, name, value):
		if name in self.keys():
			self[name] = value
			return value
		else:
			object.__setattr__(self, name, value)

	def __delattr__(self, name):
		try:
			return object.__delattr__(self, name)
		except AttributeError:
			return self.pop(name, None)
					
	def __repr__(self):
		return '<%s: %s>' %(self.__class__.__name__, len(self.keys()))

	def __hash__(self):
		import copy
		
		def hash_helper(obj):
			if isinstance(obj, (set, tuple, list)):
				return tuple([hash_helper(element) for element in obj])    

			elif not isinstance(obj, dict):
				return hash(obj)

			new_obj = {}

			for key, value in obj.items():
				new_obj[key] = hash_helper(value)

			return hash(tuple(frozenset(sorted(new_obj.items()))))

		return hash_helper(self)

	def dir(self):
		tree_map = ['   .%s\t%s' %(key, type(value)) for key, value in self.items()]
		print('Attributes (Keys) map:\n%s' %('\n'.join(tree_map).expandtabs(30)))

	def factory(self, factory_type):
		self.default_factory = factory_type

	def lock(self):
		self.default_factory = None

	
	
class AbstractObject(object):
	# - IO
	def fromDict(self, dictionary):
		raise NotImplementedError

	# - Scenery
	def getDescription(self):
		raise NotImplementedError

	# - Inventory
	def getItems(self):
		raise NotImplementedError
	
	# - Movement
	def goNorth(self):
		raise NotImplementedError

	def goSounth(self):
		raise NotImplementedError

	def goEast(self):
		raise NotImplementedError

	def goWest(self):
		raise NotImplementedError

	def goUp(self):
		raise NotImplementedError

	def goDown(self):
		raise NotImplementedError


class Room(AbstractObject):
	pass


class Item(AbstractObject):
	pass


class Actor(AbstractObject):
	pass
