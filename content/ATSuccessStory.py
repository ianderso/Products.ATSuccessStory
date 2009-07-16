# -*- coding: utf-8 -*-
#
# File: ATSuccessStory.py
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
from Products.ATSuccessStory.content.ATSuccessStoryFolder import ATSuccessStoryFolder
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

    ImageField(
        name='Image',
        widget=ImageWidget(
            label='Image',
            label_msgid='ATSuccessStory_label_Image',
            i18n_domain='ATSuccessStory',
        ),
        required=1,
        storage=AttributeStorage(),
        sizes={'large'   : (768, 768),                        'preview' : (400, 400),                        'mini'    : (200, 200),                        'dot'   : (185, 185),                        'thumb'   : (128, 128),                        'tile'    :  (64, 64),                        'icon'    :  (32, 32),                        'listing' :  (16, 16),                       }
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ATSuccessStory_schema = BaseSchema.copy() + \
    getattr(ATSuccessStoryFolder, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ATSuccessStory(BaseContent, ATSuccessStoryFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),) + (getattr(ATSuccessStoryFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Success Story'

    meta_type = 'ATSuccessStory'
    portal_type = 'ATSuccessStory'
    allowed_content_types = [] + list(getattr(ATSuccessStoryFolder, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 0
    content_icon = 'ssicon.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Success Story"
    typeDescMsgId = 'description_edit_atsuccessstory'

    _at_rename_after_creation = True

    schema = ATSuccessStory_schema

    ##code-section class-header #fill in your manual code here
    #security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('Image').tag(self, **kwargs)
    ##/code-section class-header

    # Methods

    # Manually created methods

    #security.declareProtected(View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('Image').tag(self, **kwargs)
    ##/code-section class-header


registerType(ATSuccessStory, PROJECTNAME)
# end of class ATSuccessStory

##code-section module-footer #fill in your manual code here
##/code-section module-footer



