# -*- coding: utf-8 -*-
#
# File: testATSuccessStoryFolder.py
#
# Copyright (c) 2007 by ['Franco Pellegrini']
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Franco Pellegrini <frapell@menttes.com>"""
__docformat__ = 'plaintext'

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) ATSuccessStoryFolder
#

from Testing import ZopeTestCase
from Products.ATSuccessStory.config import *
from Products.ATSuccessStory.tests.testPlone import testPlone

# Import the tested classes
from Products.ATSuccessStory.content.ATSuccessStoryFolder import ATSuccessStoryFolder

##code-section module-beforeclass #fill in your manual code here
from Products.CMFPlone.utils import _createObjectByType

##/code-section module-beforeclass


class testATSuccessStoryFolder(testPlone):
    """Test-cases for class(es) ATSuccessStoryFolder."""

    ##code-section class-header_testATSuccessStoryFolder #fill in your manual code here
    ##/code-section class-header_testATSuccessStoryFolder

    def afterSetUp(self):
        pass

    def testOnlyAllowSS(self):
        id = 'folder-test1'
        _createObjectByType('ATSuccessStoryFolder', self.portal, id=id, title="A success stories folder")
        atssf = getattr(self.portal, id, None)
        self.failUnless(len(atssf.allowed_content_types) == 1)
        self.failUnless((atssf.allowed_content_types)[0] == 'ATSuccessStory')

    # Manually created methods


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testATSuccessStoryFolder))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


