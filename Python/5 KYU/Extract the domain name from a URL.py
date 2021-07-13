def domain_name(url):
    if 'www' not in url and '//' in url :
        if 'https://' in url:
            tes = url.split('https://')
            tes2 = tes[1].split('.')
            return tes2[0]
        else:
            tes = url.split('http://')
            tes2 = tes[1].split('.')
            return tes2[0]
            
    elif 'www' in url:
        tes = url.split('.')
        return tes[1]
    else:
        tes = url.split('.')
        return tes[0]
