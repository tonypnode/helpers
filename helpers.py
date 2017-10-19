import re


def macaddr_parse(mac_string, chunk=3, delimiter='-', upper=True):
    """ Parses and validates any usual MAC address format and returns one per configured params"""
    wash = re.sub(r'[^A-Fa-f0-9]+', '', mac_string)
    if len(wash) != 12:
        raise ValueError('Incorrect MAC Address format: Should be 12 Hex chars')
    else:
        dry = delimiter.join((wash[i:i+chunk] for i in range(0, len(wash), chunk)))
        if upper:
            return dry.upper()
        else:
            return dry

mac_addr_list = {
            '1234567890af': '1234-5678-90AF',
            'fFdD.EabC.1290': 'FFDD-EABC-1290',
            'FDE abc 098.432': 'FDEA-BC09-8432',
        }
for k, v in mac_addr_list.items():
    print(k, v)
