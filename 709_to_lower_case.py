

def toLowerCase(str : str) -> str:
    s = ''
    for c in str:
        asci_val = ord(c)
        if 65 <= asci_val <= 90:
            s += chr(asci_val+32)
        else:
            s += c
    return s