from zope.i18nmessageid import MessageFactory
PloneMessageFactory = MessageFactory('plone')

from Products.CMFCore.permissions import setDefaultRoles
setDefaultRoles('signature.portlets.gdsignature: Add GroupDocs Signature portlet',
                ('Manager', 'Site Administrator', 'Owner',))
