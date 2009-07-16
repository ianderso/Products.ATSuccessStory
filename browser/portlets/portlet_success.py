from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.ATSuccessStory.browser.interfaces import ISuccessStoryPortlet

import random

class SuccessStoryPortlet(utils.BrowserView):
    implements(ISuccessStoryPortlet)

    def success(self):
        context = utils.context(self)
        portal_catalog = getToolByName(context, "portal_catalog")

        results = []
        paths = []                  #where i will load the paths where i should search for atss

        success_local = context.getProperty('local_success')

        if success_local:
            for i in success_local:
                site_path = ('/'.join(context.portal_url.getPhysicalPath()[:-1]))+'/'
                paths.append(site_path+i)

        if not(context.meta_type=='ATFolder' or context.meta_type=='ATSuccessStoryFolder' or context.meta_type == 'ATBTreeFolder' or context.meta_type=='Plone Site'):
            context = context.getParentNode()

        paths.append(('/'.join(context.getPhysicalPath()))+'/success-stories')

        for path in paths:
            result = portal_catalog.searchResults(meta_type='ATSuccessStory', path = path)
            for i in result:
                results.append(i)

        if results:
            return random.choice(results)
        else:
            return None

    def success_global(self):
        context = utils.context(self)
        portal_catalog = getToolByName(context, "portal_catalog")

        results = []
        paths = []                  #where i will load the paths where i should search for atss

        success_local = context.getProperty('local_success')

        if not success_local:
            success_local = ()

        success_global = context.portal_properties.site_properties.getProperty('global_success')
        if not success_global:
            success_global = ()
        success_global = success_global + success_local

        success_global = context.unique(success_global)

        if success_global:
            for i in success_global:
                site_path = ('/'.join(context.portal_url.getPhysicalPath()[:-1]))+'/'
                paths.append(site_path+i)

        if not(context.meta_type=='ATFolder' or context.meta_type=='ATSuccessStoryFolder' or context.meta_type == 'ATBTreeFolder' or context.meta_type=='Plone Site'):
            context = context.getParentNode()

        paths.append(('/'.join(context.getPhysicalPath()))+'/success-stories')

        for path in paths:
            result = portal_catalog.searchResults(meta_type='ATSuccessStory', path = path)
            for i in result:
                results.append(i)

        if results:
            return random.choice(results)
        else:
            return None

    def list_success(self, port_type, from_id):
        context = utils.context(self)
        portal_catalog = getToolByName(context, "portal_catalog")

        results = []
        paths = []                  #where i will load the paths where i should search for atss

        #context = context.getParentNode()
        if context.getId() == from_id:
            local = context
        else:
            local = getattr(context, from_id)
        
        if not(local.meta_type=='ATFolder' or local.meta_type=='ATSuccessStoryFolder' or local.meta_type == 'ATBTreeFolder' or context.meta_type=='Plone Site'):
            local = local.getParentNode()

        success_local = local.getProperty('local_success')
        if not success_local:
            success_local = ()

        if port_type == 'global':
            success_global = context.portal_properties.site_properties.getProperty('global_success')
            if not success_global:
                success_global = ()
        elif port_type == 'local':
            success_global = ()

        success = success_local + success_global

        success = context.unique(success)

        if success:
            for i in success:
                site_path = ('/'.join(context.portal_url.getPhysicalPath()[:-1]))+'/'
                paths.append(site_path+i)

        paths.append(('/'.join(local.getPhysicalPath()))+'/success-stories')

        for path in paths:
            result = portal_catalog.searchResults(meta_type='ATSuccessStory', path = path)
            for i in result:
                results.append(i)

        if results:
            return results
        else:
            return ()