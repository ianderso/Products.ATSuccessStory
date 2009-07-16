from zope.interface import Interface, Attribute

class ISuccessStoryPortlet(Interface):
    """Interface for portlet to display Success Stories.
    """
    def success(self):
        """this method returns success stories located under 'success-stories' folder"""

    def success_global(self):
        """this method returns success stories located under 'success-stories' folder, and the
        folders listed in the 'global_success' property"""

    def list_success(self, port_type, from_id):
        """this method returns a list with all success stories that are possible to be shown in the
        portlet from where it was called"""