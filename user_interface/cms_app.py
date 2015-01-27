from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class UIApphook(CMSApp):
    name = _("UI Apphook")
    urls = ["user_interface.urls"]

apphook_pool.register(UIApphook)