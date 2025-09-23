#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
import hashlib
class Codec:

    def __init__(self) -> None:
        self.url_db = {}
        self.id = 10000

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_url = hashlib.md5(longUrl.encode(encoding='UTF-8')).hexdigest()
        if short_url not in self.url_db:
            self.url_db[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_db[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

