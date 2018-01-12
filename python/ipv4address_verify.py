import ipaddress

debug_msg = "Debug:"
debug = True


def verify_ipv4_address(ipv4addr):
    '''
    Verifies IPv4 addresses.
    Returns True or False
    '''
    try:
        ipaddress.IPv4Address(ipv4addr)
    except ipaddress.AddressValueError as e:
        if debug is True:
            print(e)
        return False
    else:
        return True
