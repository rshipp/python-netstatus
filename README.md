This project is documented extensively with Python docstrings. PyDoc is
used to convert these docstrings into text format for use outside of a
Python interpreter.

See [objects.pydoc](docs/objects.pydoc) for information about
the objects package.

See [networkobject.pydoc](docs/networkobject.pydoc) for
information about the NetworkObject base class.

See [httpserver.pydoc](docs/httpserver.pydoc) for information
about the HTTPServer class, which inherits from NetworkObject.

See status.py for an extremely basic example of how to use this module.

Implementation details may change at any time, so don't depend on
anything that isn't documented. I may also switch to using kwargs
instead of ordered arguments for function calls and/or object
instantiations, if it seems like that would be useful. For now, I'm
working on the assumption that "you aren't gonna need it."
