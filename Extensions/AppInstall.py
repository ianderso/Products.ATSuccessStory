# -*- coding: utf-8 -*-
#

__author__ = """Franco Pellegrini <frapell@menttes.com>"""
__docformat__ = 'plaintext'


from Products.CMFCore.utils import getToolByName

def install(portal):
    prop = getToolByName(portal,'portal_properties') 
    
    if not (prop.site_properties.hasProperty('global_success')):
        prop.site_properties.manage_addProperty(id="global_success", 
                                                type='lines',
                                                value=())
    return