# -*- coding: utf-8 -*-
#
# File: ATSuccessStory.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.5.0
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
from Products.ATContentTypes.content.image import ATImage
from Products.ATSuccessStory.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='Story',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Story',
            label_msgid='ATSuccessStory_label_Story',
            i18n_domain='ATSuccessStory',
        ),
        default_output_type='text/html',
        required=1
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ATSuccessStory_schema = getattr(ATImage, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here

##ATSuccessStory_schema.moveField('image', pos='bottom')
ATSuccessStory_schema.moveField('relatedItems', pos='bottom')
ATSuccessStory_schema.moveField('allowDiscussion', pos='bottom')

##/code-section after-schema

class ATSuccessStory(ATImage):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATImage,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Success Story'

    meta_type = 'ATSuccessStory'
    portal_type = 'ATSuccessStory'
    allowed_content_types = [] + list(getattr(ATImage, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'ATSuccessStory.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Success Story"
    typeDescMsgId = 'description_edit_atsuccessstory'

    _at_rename_after_creation = True

    schema = ATSuccessStory_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ATSuccessStory, PROJECTNAME)
# end of class ATSuccessStory

##code-section module-footer #fill in your manual code here
##/code-section module-footer



