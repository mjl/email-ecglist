# ------------------------------------------------------------------------
# coding=utf-8
# ------------------------------------------------------------------------
#
#  Created by Martin J. Laubach on 2013-03-17
#  Copyright (c) 2013 Martin J. Laubach. All rights reserved.
#
# ------------------------------------------------------------------------

from __future__ import absolute_import

import os
import sys

import unittest

sys.path.insert(0, os.path.abspath('..'))

from ecglist import ECGList

# ------------------------------------------------------------------------
class EcglistTest(unittest.TestCase):
    testlist_emails     = ('karl.testinger@firma.at', 'max.mustermann@home.at')
    testlist_not        = ('karl.testinger@firmu.ut', 'mix.mustermann@home.at')
    testlist_domains    = ('foo@home.lan', 'bar@firma.lan')
    testlist_notdomains = ('foo@home.lon', 'max.mustermann@farma.lan')

    def setUp(self):
        self.ecglist = ECGList(filename="tests/testliste.hash")

    def test_01_emails(self):
        for email in self.testlist_emails:
            self.assertEqual(self.ecglist.get_blacklist_status(email, numeric=True), ECGList.ADDRESS_BLACKLISTED)
            s = self.ecglist.get_blacklist_status(email)
            self.assertIsNotNone(s)
            self.assertIsInstance(s, basestring)

    def test_02_not_emails(self):
        for email in self.testlist_not:
            self.assertIsNone(self.ecglist.get_blacklist_status(email, numeric=True))
            self.assertIsNone(self.ecglist.get_blacklist_status(email))

    def test_03_domains(self):
        for email in self.testlist_domains:
            self.assertEqual(self.ecglist.get_blacklist_status(email, numeric=True), ECGList.DOMAIN_BLACKLISTED)
            s = self.ecglist.get_blacklist_status(email)
            self.assertIsNotNone(s)
            self.assertIsInstance(s, basestring)

    def test_04_not_domains(self):
        for email in self.testlist_notdomains:
            self.assertIsNone(self.ecglist.get_blacklist_status(email, numeric=True))
            self.assertIsNone(self.ecglist.get_blacklist_status(email))

    def test_05_email_syntax(self):
        email = "foobar.baz"
        self.assertEqual(self.ecglist.get_blacklist_status(email, numeric=True), ECGList.NOT_EMAIL_ADDRESS)
        s = self.ecglist.get_blacklist_status(email)
        self.assertIsNotNone(s)
        self.assertIsInstance(s, basestring)

    def test_06_in_operator(self):
        self.assertFalse(self.testlist_not[0] in self.ecglist)
        self.assertTrue(self.testlist_emails[0] in self.ecglist)

    def test_07_subscript_operator(self):
        self.assertIsNone(self.ecglist[self.testlist_not[0]])
        self.assertEquals(self.ecglist[self.testlist_emails[0]], ECGList.ADDRESS_BLACKLISTED)

# ------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------------
