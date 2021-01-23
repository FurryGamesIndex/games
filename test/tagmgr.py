#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# Copyright (C) 2020 Utopic Panther
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

import unittest
import yaml
from copy import deepcopy

from fgi.tagmgr import TagManager

class test_tagmgr(unittest.TestCase):

    tagdep = {
        "ns1": {
            "a": [ "b" ],
            "b": [ "c", "f", "g" ],
            "c": [ "d", "e", "k" ],
            "h": [ "i", "j" ],
            "k": [ "l" ],
        },
        "ns2": {
            "aa": [ "ns2some", "ns1:c" ],
            "bb": [ "aa" ],
            "cc": [ "bb", "ns1:b" ],
            "dd": [ "ns1:k", 'ns3:ns3some' ],
        }
    }

    result = {
        'ns1': {
            'a': {'c', 'd', 'f', 'b', 'e', 'g', 'k', 'l'},
            'b': {'c', 'd', 'f', 'e', 'g', 'k', 'l'},
            'c': {'e', 'd', 'k', 'l'},
            "h": {'i', 'j'},
            "k": {'l'},
        },
        'ns2': {
            'aa': {'ns1:c', 'ns1:e', 'ns1:d', 'ns1:k', 'ns1:l', 'ns2some'},
            'bb': {'aa', 'ns1:d', 'ns1:c', 'ns1:e', 'ns1:k', 'ns1:l', 'ns2some'},
            'cc': {'aa', 'bb', 'ns1:b', 'ns1:c', 'ns1:d', 'ns1:e', 'ns1:f', 'ns1:g', 'ns1:k', 'ns1:l', 'ns2some'},
            'dd': {'ns1:k', 'ns1:l', 'ns3:ns3some'},
        }
    }

    def test_closure(self):
        tagmgr = TagManager()

        tagmgr.loaddep(test_tagmgr.tagdep)
        tagmgr.closure_all_tagdep()

        self.assertDictEqual(test_tagmgr.result, tagmgr.tagdep)

if __name__ == '__main__':
    unittest.main()
