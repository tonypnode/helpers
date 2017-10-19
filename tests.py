import unittest
import helpers


class HelpersTests(unittest.TestCase):

    def test_mac_parse(self):
        mac_addr_list = {
            '1234567890af': '1234-5678-90AF',
            'fFdD.EabC.1290': 'FFDD-EABC-1290',
            'FDE abc 098.432': 'FDEA-BC09-8432',
        }

        for k, v in mac_addr_list.items():
            self.assertEqual(helpers.macaddr_parse(k, chunk=4, delimiter='-', upper=True), v)
