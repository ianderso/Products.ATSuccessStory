from zope.interface import Interface, Attribute

class ISuccessStoryPortlet(Interface):
    """Interface for portlet to display Success Stories.
    """
    def published_success_stories(self, folder):
        """This script returns Success Stories from the specified folder.
        """