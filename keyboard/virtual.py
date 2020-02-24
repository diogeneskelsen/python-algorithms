"""Model objects for requests and responses.

Each API may support one or more serializations, such
as JSON, Atom, etc. The model classes are responsible
for converting between the wire format and the Python
object representation.
"""

__author__ = "diogeneskelsen@gmail.com (Diogenes Kelsen)"

class Virtual(object):
    """Virtual class.

  All Model classes should implement this interface.
  The Model serializes and de-serializes between a wire
  format such as JSON and a Python object representation.
  """

    def session(self, parameter_list):
      pass

    def funcname(self, parameter_list):
      pass

    def validate(self, parameter_list):
      pass
