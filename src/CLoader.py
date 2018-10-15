import cffi
import importlib


def load(filename):
	source = open(filename + '.c').read()
	includes = open(filename + '.h').read()
	
	ffibuilder = cffi.FFI()
	ffibuilder.cdef(includes)
	ffibuilder.set_source(filename + '_', source)
	ffibuilder.compile()

	module = importlib.import_module(filename + '_')
	return module.lib
