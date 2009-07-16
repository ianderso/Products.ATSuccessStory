## Script (Python) "successResult"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

result = context.portal_catalog.searchResults(portal_type='ATSuccessStory', review_state='published')

return result
