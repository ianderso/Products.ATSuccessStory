from zope.interface import Interface
from zope.component import getMultiAdapter

from zope.interface import implements
from zope.component import getUtility

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from plone.i18n.normalizer.interfaces import IIDNormalizer

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone import utils
from Products.CMFCore.utils import getToolByName

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from Products.ATContentTypes.interface import IATFolder

from plone.memoize.instance import memoize

from zope.i18nmessageid import MessageFactory

import random

successStoryPortletMessageFactory = MessageFactory('Products.ATSuccessStory')
_ = successStoryPortletMessageFactory


class IsuccessStoryPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    header = schema.TextLine(title=_(u"Header"),
                                  description=_(u"Portlet header"),
                                  required=True)

    searchpath = schema.Choice(title=_(u"Stories Path"),
                                  description=_(u"Search for success stories inside this path"),
                                  required=True,
                                  source=SearchableTextSourceBinder({'object_provides' : IATFolder.__identifier__}))

    number_of_stories = schema.Int(title=_(u"Number of stories"),
                                        description=_(u"Specify how many Success Stories you want displayed at the same time in the portlet. Most commonly you will need 1."),
                                        required=True)

    global_portlet = schema.Bool(title=_(u"Global"),
                                 description=_(u"Is this a global portlet? this will cause not only to search using the search path, but to search for stories from the whole site."),
                                 default=False)
class Assignment(base.Assignment):
    """Portlet assignment.
    
    This is what is actually managed through the portlets UI and associated
    with columns.
    """
    
    implements(IsuccessStoryPortlet)
    
    # When you introduce new attributes, you need to make sure old portlets
    # also have these new attributes. You do that by adding them here.
    # Otherwise, installing a new version will break the site.
    number_of_stories = 1
    global_portlet = False

    def __init__(self,
                 header='Success Stories',
                 searchpath='/',
                 number_of_stories=1,
                 global_portlet=False):

        self.header = header
        self.searchpath = searchpath
        self.number_of_stories = number_of_stories
        self.global_portlet = global_portlet


    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave.
        """
        return _(u"Success Story Portlet")

class Renderer(base.Renderer):
    """Portlet renderer.
    
    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('../templates/portlet_success.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.portal_url = portal_state.portal_url()
        self.portal = portal_state.portal()

    def search_stories(self):
        folder_path = self.get_searchpath()

        if folder_path:
            if not self.global_portlet:
                results = self.context.portal_catalog(path = folder_path, portal_type = 'ATSuccessStory')
            else:
                results = self.context.portal_catalog(portal_type = 'ATSuccessStory')

            if results:
                shuffled = list(results)
                random.shuffle(shuffled)
                return shuffled[:self.number_of_stories]
            else:
                return None
        else:
            return None

    @property
    def header(self):
        return self.data.header

    @property
    def number_of_stories(self):
        return int(self.data.number_of_stories)

    @property
    def global_portlet(self):
        return self.data.global_portlet

    @memoize
    def get_searchpath(self):
        folder = self.get_search_folder()
        if IATFolder.providedBy(folder):
            return '/'.join(folder.getPhysicalPath())
        else:
            return None
        
    @memoize
    def get_search_folder(self):
        if self.global_portlet:
            return self.portal
        folder_path = self.data.searchpath

        if folder_path[0]=='/':
            folder_path = folder_path[1:]

        return self.portal.restrictedTraverse(folder_path, default=None)
    
    def get_folder_link(self):
        return self.get_search_folder().absolute_url()
    

class AddForm(base.AddForm):
    """Portlet add form.
    
    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IsuccessStoryPortlet)
    label = _(u"Add Success Story Portlet")
    description = _(u"This portlet displays a random success story")
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment

class EditForm(base.EditForm):
    """Portlet edit form.
    
    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IsuccessStoryPortlet)
    label = _(u"Add Success Story Portlet")
    description = _(u"This portlet displays a random success story")