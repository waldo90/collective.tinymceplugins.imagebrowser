from zope import schema
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.tinymceplugins.imagebrowser')


class ITinyMCELibrariesImageResources(Interface):
    """Plone registry entries to register TinyMCE image browser resources.
    """

    imagebrowser_resources = schema.List(title=_(u"Image Resources"),
                              required=False,
                              value_type=schema.TextLine(),
                              default=[],
                              missing_value=[])
    
    imagebrowser_default_resource = schema.TextLine(title=_(u"Default Image Resource"),
                                    required=False,
                                    default=u'',
                                    missing_value=u'')
