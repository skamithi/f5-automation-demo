#!/usr/bin/python

import unittest
from ansible.module_utils.six import iteritems
import netaddr

def enable_snat(self_ip_data, port_members):
    """
    Check if any port member is not part of the self_ip network pool
    Return: Automap if if SNAT should be enabled
    """
    count = 0
    for (net_entry,value) in iteritems(self_ip_data):
        ipnet = netaddr.IPNetwork("%s/%s" %(value.get('address'), value.get('netmask')))
        ipset = netaddr.IPSet(ipnet)
        for port_member in port_members:
            if port_member in ipset:
                count = count + 1
    if len(port_members) == count:
        return 'None'
    return 'Automap'


class FilterModule(object):
    """ This filter plugin takes F5 self_ip info and check to see if
    the port member IPs are in the self_ip network ranges. If port member IP
    is not in any of the self_ip ranges then this module returns 'None'
    Example:
       self_ip | enable_snat(['10.1.1.1','10.10.1.1'])

    """

    def filters(self):
        return {
            'enable_snat': enable_snat
        }


class TestGetCapsuleID(unittest.TestCase):
    """
    test case for this filter plugin. to execute
    run ``python enable_snat.py``
    """
    def test_enable_snat(self):
        data = {
            "/common/10.1.1.1": {
                "address": "10.1.1.1",
                "netmask": "255.255.255.0"
            },
            "/common/10.100.1.1": {
                "address": "10.100.1.1",
                "netmask": "255.255.252.0"
            },
            "/common/10.200.1.10": {
                "address": "10.200.1.10",
                "netmask": "255.255.255.128"
            },
            "/common/10.110.20.1": {
                "address": "10.110.20.1",
                "netmask": "255.255.255.192"
            }
        }
        self.assertEqual(enable_snat(data,
                        ['10.1.100.1', '10.140.1.10']), 'Automap')
        self.assertEqual(enable_snat(data,
                        ['10.100.1.10', '10.200.1.20']), 'None')


if __name__ == '__main__':
    unittest.main()
