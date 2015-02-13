class lexicon:
    @staticmethod
    def scan(s):
        return [('direction',x) for x in s.split()]

print(lexicon.scan("north south east"))
