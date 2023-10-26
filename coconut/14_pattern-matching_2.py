def type(x):
    _coconut_match_to = x
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
        a = _coconut_match_to[0]
        b = _coconut_match_to[1]
        _coconut_match_check = True
    if _coconut_match_check:
        return "list, 2 items"
    if not _coconut_match_check:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 1):
            a = _coconut_match_to[0]
            _coconut_match_check = True
        if _coconut_match_check:
            return "list, 1 item"
    if not _coconut_match_check:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 0):
            _coconut_match_check = True
        if _coconut_match_check:
            return "empty list"

def say_hello(s):
    _coconut_match_to = s
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.startswith("My name is ")):
        name = _coconut_match_to[_coconut.len("My name is "):]
        _coconut_match_check = True
    if _coconut_match_check:
        return "Hi " + name

def pair(p):
    _coconut_match_to = p
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == _coconut_match_to[1]):
        x = _coconut_match_to[0]
        _coconut_match_check = True
    if _coconut_match_check:
        return "same values!"
    if not _coconut_match_check:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check and not (x > y):
            _coconut_match_check = False
        if _coconut_match_check:
            return "1st value is greater"
    if not _coconut_match_check:
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2):
            x = _coconut_match_to[0]
            y = _coconut_match_to[1]
            _coconut_match_check = True
        if _coconut_match_check:
            return "2nd value is greater"
    if not _coconut_match_check:
        return "other"

def get_name(s):
    _coconut_match_to = s
    _coconut_match_check = False
    if (_coconut.isinstance(_coconut_match_to, _coconut.str)) and (_coconut_match_to.endswith("@root.cz")):
        name = _coconut_match_to[:-_coconut.len("@root.cz")]
        _coconut_match_check = True
    if _coconut_match_check:
        return name

