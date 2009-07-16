Description

    ATSuccessStory provides a custom content type that allows to add 'Success Stories' to a Plone Site
    it also provides 2 portlets and a custom view

Installation

    Place the ATSuccessStory folder inside the Products' folder of your zope instance and install
    using the "portal_quickinstaller"

Usage

    The success stories can only be added inside a 'Success Story Folder', so the first
    thing to do should be add one of this folders.
    So go to your site, click on "Add to folder", add one "success story folder", and then you'll
    be able to add 'success stories'.

Portlets

    the product provides 2 portlets, 'portlet_success' and 'portlet_success_global'.
    To use them, you have to go to the ZMI and add one or both to a 'left_slot' or 'right_slot'

    here/portlet_success/macros/portlet
    here/portlet_success_global/macros/portlet

portlet_success

    This portlet works as follows, it searchs for 'success stories' located inside a 'success
    stories folder' named exactly 'success-stories', and it shows a random one.
    Also, you can add a property to the object where the portlet is shown, called 'local_success'
    this should be a lines type field, and there you will add 'success stories folders' from where
    you want to search for success stories.

    For Example, let's say your site's root is at:

    http://your.host:9192/site/www

    so, if you want the portlet to be shown at root level, you should add a folder whom URL would be

    http://your.host:9192/site/www/success-stories

    where you will load all success stories.
    all stories located there will be shown in the portlet.

    Let's say that you have another success stories folder where you have more stories, located at

    http://your.host:9192/site/www/my-folder/folder2/stories

    that you want them to be shown in a portlet located at 

    http://your.host:9192/site/www/testing1/testing2/

    then you go to the ZMI, and go to the 'testing2' folder, click on 'properties', then
    add a new propertie called 'local_success' of type lines, and then you should add a new line

    my-folder/folder2/stories

    notice how we omitted 'http://your.host:9192/site/www/' and also there's no final slash.
    you can add to this property as many folders as you want, always in that format.
    The portlet will search success stories in all these folders (also folder named 'success-stories')
    and show a random one

portlet_success_global

    This works exactly as 'portlet_success' with the only difference that, it not only searches for
    stories inside a folder called 'success-stories' and the 'local_success' propertie, but it also
    searches for stories located in folders listed on a property that's inside
    'portal_properties/site_properties' called 'global_success'

    The way to use 'global_success' property is the same as the 'local_success' property explained before.

I hope i was clear with my explanation, if not, just mail me :-D

Author

  Franco Pellegrini <frapell@menttes.com>
