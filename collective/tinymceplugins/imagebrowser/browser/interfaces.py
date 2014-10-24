from zope import schema
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.tinymceplugins.imagebrowser')
 

class ITinymceImageBrowser(Interface):
    """Marker interface to override tinymce default views."""


class ITinyMCELibrariesExtended(Interface):

    imagebrowser_resources = schema.Text(
        title=_(u"Image Resources", default="Image Resources"),
        description=_(u"Image Resources Description", 
                      default=u"Enter a list of resources to appear in the link"
                              u" image dialog. The format is "
                              u"id|title|path_to_folder|path_to_icon, one per "
                              u"line. An example path_to_folder is "
                              u"'Plone/picture', an example path_to_icon is "
                              u"'/logoIcon.gif'. The path_to_icon is optional."
                     ),
        required=False)
    
    imagebrowser_default_resource = schema.TextLine(
        title=_(u"Default Image Resource (Optional)", default=u"Default Image Resource (Optional)"),
        description=_(u"Default Image Resource Description",
                      default=u"Enter the 'id' of one of the above image "
                              u"resources to make it the default starting folder. "
                              u"Leave blank to start in the current folder."),
        required=False)
