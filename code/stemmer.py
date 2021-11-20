import sys

class Porter():

    consonants = "bcdfghjklmnpqrstwxz"
    vowels = "aeiou"
    neither = "y"
    endings2 = [('ational','ate'), ('tional','tion'), ('enci','ence'), ('anci','ance'), ('izer', 'ize'), ('abli','able'), ('alli','al'), ('entli', 'ent'), ('eli', 'e'), ('ousli', 'ous'), ('ization', 'ize'), ('ation', 'ate'), ('ator', 'ate'), ('alism', 'al'), ('iveness', 'ive'), ('fulness', 'ful'), ('ousness', 'ous'), ('aliti','al'), ('ivit', 'ive'), ('biliti','ble')]
    endings3 = [('icate','ic'),('ative',''),('alize','al'),('iciti','ic'),('ical','ic'),('ful',''),('ness','')]
    suffixes4a = ['al','ance','ence','er','ic','able','ible','ant','ement','ment','ent']
    suffix_special = 'ion'
    suffixes4b = ['ou','ism','ate','iti','ous','ive','ize']


    def stem(self, word):
        stem = self._step1(word)
        stem = self._step2(stem)
        stem = self._step3(stem)
        stem = self._step4(stem)
        stem = self._step5(stem)
        return stem

    def _group(self, word):
        grouping = []
        previous = ""
        for index, character in enumerate(word):
            if previous == "":
                previous = character
            else:
                if self._compare_same_class(previous, character):
                    previous += character
                    if index == len(word)-1:
                        grouping.append(previous)
                else:
                    grouping.append(previous)
                    previous = character
                    if index == len(word)-1:
                        grouping.append(character)
        return grouping

    def _compare_same_class(self, char1, char2):
        if char1 in self.consonants and char2 in self.consonants:
            return True
        elif char1 in self.vowels and char2 in self.vowels:
            return True
        return False
    
    def _classify(self, grouping):
        return "C" if grouping[0] in self.consonants else "V"

    def _remove_endings(self, word, substitutions):
        if self._det_m(word) > 0:
            for phrase, substitution in substitutions:
                if word.endswith(phrase):
                    return word[:-len(phrase)]+substitution
        return word

    def _reduce(self, word):
        encoded = self._group(word)
        return [self._classify(group) for group in encoded]

    def _det_m(self, word):
        classes = self._reduce(word)
        if len(classes) < 2:
            return 0
        if classes[0] == 'C':
            classes = classes[1:]
        if classes[-1] == 'V':
            classes = classes[:len(classes)-1]
        if (len(classes)/2) >= 1:
            return len(classes)//2
        else:
            return 0

    def _chk_LT(self, stem, lt):
        for letter in lt:
            if stem.endswith(letter):
                return True
        return False

    def _chk_v(self, stem):
        for letter in stem:
            if letter in self.vowels:
                return True
        return False

    def _chk_d(self, stem):
        if stem[-1] in self.consonants and stem[-2] in self.consonants:
            return True
        return False

    def _chk_o(self, stem):
        if len(stem) <3:
            return False
        if (stem[-3] in self.consonants) and (stem[-2] in self.vowels) and (stem[-1] in self.consonants) and (stem[-1] not in "wxy"):
            return True
        return False

    def _step1(self, word):
        # 1a
        if word.endswith('sses'):
            word = word[:-2]
        elif word.endswith('ies'):
            word = word[:-2]
        elif not word.endswith('ss') and word.endswith("s"):
            word = word[:-1]
        
        # 1b1
        b2 = False
        if len(word) > 4:
            if word.endswith("eed") and self._det_m(word) > 0:
                word = word[:-1]
            elif word.endswith("ed"):
                word = word[:-2]
                if self._chk_v(word):
                    b2 = True
            elif word.endswith("ing"):
                word = word[:-3]
                if self._chk_v(word):
                    b2 = True
        # 1b2
        if b2:
            if word.endswith("at") or word.endswith("bl") or word.endswith("iz"):
                word += "e"
            elif self._chk_d(word) and not (self._chk_LT(word,"lsz")):
                word = word[:-1]
            elif self._det_m(word)==1 and self._chk_o(word):
                word += "e"
        # 1c
        if self._chk_v(word) and word.endswith('y'):
            word = word[:-1]+'i'
        
        return word

    def _step2(self, word):
        return self._remove_endings(word, self.endings2)

    def _step3(self, word):
        return self._remove_endings(word, self.endings3)

    def _step4(self, word):
        if self._det_m(word)>1:
            for suffix in self.suffixes4a :
                if word.endswith(suffix):
                    return word[:-len(suffix)]
            if word.endswith(self.suffix_special):
                temp = word[:-len(self.suffix_special)]
                if self._chk_LT(temp, 'st'):
                    return temp
            for suffix in self.suffixes4b:
                if word.endswith(suffix):
                    return word[:-len(suffix)]
        return word

    def _step5(self, word):
        # 5a
        if self._det_m(word)>1 and word.endswith('e'):
            word = word[:-1]
        elif self._det_m(word) == 1 and (not self._chk_o(word)) and word.endswith('e') and len(word) > 4:
            word = word[:-1]
        # 5b
        if self._det_m(word) > 1 and self._chk_d(word) and self._chk_LT(word, 'l'):
            word = word[:-1]
        return word