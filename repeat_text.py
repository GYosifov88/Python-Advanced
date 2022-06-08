# try:
#     text = input()
#     times = int(input())
#     print(text * times)
#
# except ValueError:
#     print("Variable times must be an integer")
#

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error, "Raised when the input value is too small"):
   """Raised when the input value is too small"""

num = int(input())
if num < 10:
   raise ValueTooSmallError
