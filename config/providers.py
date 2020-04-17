"""Providers Configuration File."""
from masonite.providers import (AppProvider, AuthenticationProvider, BroadcastProvider, CacheProvider,
                                CsrfProvider, HelpersProvider, MailProvider,
                                QueueProvider, RouteProvider,
                                SessionProvider, StatusCodeProvider,
                                UploadProvider, ViewProvider,
                                WhitenoiseProvider)
from masonite.validation.providers.ValidationProvider import ValidationProvider

from masonite.logging.providers import LoggingProvider
from masonite.validation.providers import ValidationProvider

from masonite.providers import CorsProvider
from masonite.api.providers import ApiProvider

from masonite.scheduler.providers import ScheduleProvider

"""Providers List
Providers are a simple way to remove or add functionality for Masonite
The providers in this list are either ran on server start or when a
request is made depending on the provider. Take some time to can
learn more more about Service Providers in our documentation
"""

PROVIDERS = [
    # Framework Providers
    AppProvider,
    CorsProvider,
    AuthenticationProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    WhitenoiseProvider,
    ViewProvider,
    ScheduleProvider,

    # Optional Framework Providers
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    CsrfProvider,
    HelpersProvider,
    ValidationProvider,

    # Third Party Providers
    LoggingProvider,
    ValidationProvider,
    ApiProvider
    # Application Providers

]
