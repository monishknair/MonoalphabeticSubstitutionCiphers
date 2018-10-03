class AtBash(object):

    def __init__(self):
        key = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self):

        if len(self.message) < 26:
            for i in self.message:
                return self.message.replace(i, self.substitute(i))

        else:
            for i in xrange(26):
                return self.message.replace(i, self.substitute(i))

    def decrypt(self):
        return self.encrypt(self.cipher)

    def substitute(self, key):
        if self.key.find(key) < 13:
            return 26-self.val
        else:
            return None
