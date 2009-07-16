# -*- coding: utf-8 -*-
#
# File: ATSuccessStoryFolder.py
#
# Copyright (c) 2007 by []
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

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATSuccessStory.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ATSuccessStoryFolder_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ATSuccessStoryFolder(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Success Story Folder'

    meta_type = 'ATSuccessStoryFolder'
    portal_type = 'ATSuccessStoryFolder'
    allowed_content_types = ["'ATSuccessStory'"] + list(getattr(ATFolder, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 1
    #content_icon = 'ATSuccessStoryFolder.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ('summary_view',)
    typeDescription = "Success Story Folder"
    typeDescMsgId = 'description_edit_atsuccessstoryfolder'

    _at_rename_after_creation = True

    schema = ATSuccessStoryFolder_schema

    ##code-section class-header #fill in your manual code here
    allowed_content_types = ['ATSuccessStory']

    ##/code-section class-header

    # Methods


registerType(ATSuccessStoryFolder, PROJECTNAME)
# end of class ATSuccessStoryFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



