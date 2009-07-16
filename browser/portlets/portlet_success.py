from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.ATSuccessStory.browser.interfaces import ISuccessStoryPortlet

import random

class SuccessStoryPortlet(utils.BrowserView):
    implements(ISuccessStoryPortlet)

    def published_success_stories(self, folder):
        context = utils.context(self)
        portal_catalog = getToolByName(context, "portal_catalog")

        results = []
        paths = []                  #where i will load the paths where i should search for atss


        if not(context.meta_type == 'ATFolder' or context.meta_type=='ATSuccessStoryFolder' or context.meta_type == 'ATBTreeFolder') and context.getParentNode().meta_type == 'Plone Site':
            success_global = context.portal_properties.site_properties.getProperty('global_'+folder)
        else:
            success_global = context.getProperty('local_'+folder)


        if success_global:
            for i in success_global:
                site_path = ('/'.join(context.portal_url.getPhysicalPath()[:-1]))+'/'
                paths.append(site_path+i)

        if not(context.meta_type=='ATFolder' or context.meta_type=='ATSuccessStoryFolder' or context.meta_type == 'ATBTreeFolder'):
            context = context.getParentNode()

        if folder == 'partner-stories' :
            folder = 'partners/partner-stories'

        #This is ugly, with this 'if' i check if i'm at dot/www/where-we-work/COUNTRY
        if folder == 'project-showcase' and len(context.getPhysicalPath()) == 5 and context.getParentNode().id == 'where-we-work':
            #i get COUNTRY name
            country = context.getPhysicalPath()[4]
            #search folders inside dot/www/what-we-do named as the country
            featured = portal_catalog.searchResults(id=country, path = ('/'.join(context.portal_url.getPhysicalPath()[:-1]))+'/what-we-do')
            for i in featured:
                #and add the full path to the paths list
                path = (i.getPath())+'/project-showcase'
                paths.append(path)

        elif folder == 'project-showcase' and len(context.getPhysicalPath()) > 4:
            if context.getParentNode().getParentNode().id == 'what-we-do':
                pass

        else:
            paths.append(('/'.join(context.getPhysicalPath()))+'/'+folder)

        for path in paths:
            result = portal_catalog.searchResults(meta_type='ATSuccessStory', path = path)
            for i in result:
                results.append(i)

        if results:
            return random.choice(results)
        else:
            return None