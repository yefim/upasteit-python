from urllib import urlencode
from urllib2 import Request, urlopen
from json import load

DOMAIN = "http://localhost:4567/"
HEADERS = {"Accept": "application/json"}

class UPaste():
    def __init__(self, name=""):
        self.name = name

    def get(self, name=None):
        if name is None:
            name = self.name
        r = urlopen(Request(url=DOMAIN + name, headers=HEADERS))
        return load(r)

    def paste(self, *args):
        if not len(args) or len(args) > 2:
            return
        name, paste = [self.name, args[0]] if len(args) is 1 else args
        # arrays have to be encoded differently
        if isinstance(paste, basestring): 
            data = urlencode({"paste": paste})
        else:
            # see http://stackoverflow.com/questions/2571145/urlencode-an-array-of-values
            data = urlencode({"paste[]": paste}, True)
        r = urlopen(Request(url=DOMAIN + name, headers=HEADERS, data=data))
        return load(r)
