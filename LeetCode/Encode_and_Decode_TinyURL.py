import uuid


class Codec:
    def __init__(self):
        self.ram = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        code = uuid.uuid4()
        self.ram[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        result = shortUrl.split("http://tinyurl.com/")[1]
        return self.ram[result]
