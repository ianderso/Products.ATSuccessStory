

# -*- coding: utf-8 -*-
#
# File: testATSuccessStory.py
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
# Test-cases for class(es) ATSuccessStory
#

from Testing import ZopeTestCase
from Products.ATSuccessStory.config import *
from Products.ATSuccessStory.tests.testPlone import testPlone

# Import the tested classes
from Products.ATSuccessStory.content.ATSuccessStory import ATSuccessStory

##code-section module-beforeclass #fill in your manual code here
from Products.CMFPlone.utils import _createObjectByType
from Products.ATSuccessStory.browser.interfaces import ISuccessStoryPortlet

from Products.ATSuccessStory.browser.portlets.portlet_success import SuccessStoryPortlet

from Products.CMFCore.utils import getToolByName

import pdb

##/code-section module-beforeclass


class testATSuccessStory(testPlone):
    """Test-cases for class(es) ATSuccessStory."""

    ##code-section class-header_testATSuccessStory #fill in your manual code here
    ##/code-section class-header_testATSuccessStory

    def afterSetUp(self):
        self.a = 0
        self.name = 'success'+str(self.a)

    # Manually created methods

    def testOnlyInATSSFolder(self):
        self.failUnless(ATSuccessStory.global_allow == 0)

    def testSSLocalPortlet(self):
        """This test checks that the portlet shows correct content"""

        _createObjectByType('ATSuccessStoryFolder', self.portal, id=self.name, title="A success stories folder")
        atssf = getattr(self.portal, self.name, None)
        _createObjectByType('ATSuccessStory', atssf, id=self.name, title="A success story")
        view = SuccessStoryPortlet(self.portal, self.app.REQUEST)
        result = view.success()
        self.failIf(result)
        _createObjectByType('ATSuccessStoryFolder', self.portal, id='success-stories', title="A success stories folder")
        atssf = getattr(self.portal, 'success-stories', None)
        _createObjectByType('ATSuccessStory', atssf, id=self.name, title="A success story")
        ss = getattr(atssf, self.name)
        view = SuccessStoryPortlet(self.portal, self.app.REQUEST)
        result = view.success()
        self.failUnless(result)
        self.failUnless(result.id == self.name)
        self.portal.manage_delObjects([self.name, 'success-stories'])


    def testLocalSuccess(self):
        """This test checks that when having the 'local_success' setted
        it will search for SS inside those folders"""

        _createObjectByType('ATSuccessStoryFolder', self.portal, id=self.name, title="A success stories folder")
        atssf = getattr(self.portal, self.name, None)
        _createObjectByType('ATSuccessStory', atssf, id=self.name, title="A success story")
        _createObjectByType('ATSuccessStoryFolder', self.portal, id='success-stories', title="A success stories folder")
        atssf = getattr(self.portal, 'success-stories', None)
        _createObjectByType('ATSuccessStory', atssf, id=self.name, title="A success story")
        ss = getattr(atssf, self.name)
        view = SuccessStoryPortlet(self.portal, self.app.REQUEST)
        result = view.list_success('local', self.portal.id)
        self.failUnless(result)
        self.failUnless(len(result) == 1)
        self.portal.manage_addProperty(id="local_success",
                              type='lines',
                              value=(self.name,))
        view = SuccessStoryPortlet(self.portal, self.app.REQUEST)
        result = view.list_success('local', self.portal.id)
        self.failUnless(result)
        self.failUnless(len(result) == 2)
        self.portal.manage_delObjects([self.name, 'success-stories'])

    def testGlobalSuccess(self):
        """This test checks that when having the 'global_success' setted
        it will search for SS inside those folders"""

        _createObjectByType('ATSuccessStoryFolder', self.portal, id=self.name, title="A success stories folder")
        atssf = getattr(self.portal, self.name, None)
        _createObjectByType('ATSuccessStory', atssf, id=self.name, title="A success story")
        _createObjectByType('ATSuccessStoryFolder', self.portal, id='success-stories', title="A success stories folder")
        atssf = getattr(self.portal, 'success-stories', None)
        _createObjectByType('ATSuccessStory', atssf, id=self.name, title="A success story")
        ss = getattr(atssf, self.name)
        prop = getToolByName(self.portal,'portal_properties') 
        prop.site_properties.global_success = (self.name,)
        view = SuccessStoryPortlet(self.portal, self.app.REQUEST)
        result = view.list_success('local', self.portal.id)
        self.failUnless(result)
        self.failUnless(len(result) == 1)
        result = view.list_success('global', self.portal.id)
        self.failUnless(result)
        self.failUnless(len(result) == 2)
        self.portal.manage_delObjects([self.name, 'success-stories'])

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testATSuccessStory))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


