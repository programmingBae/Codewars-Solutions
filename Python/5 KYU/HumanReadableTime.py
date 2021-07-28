def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds%3600) // 60
    ss = ((seconds%3600)%60) 
    hh = str(hh).zfill(2)
    mm = str(mm).zfill(2)
    ss = str(ss).zfill(2)
    return f"{hh}:{mm}:{ss}"
