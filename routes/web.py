"""Web Routes."""

from masonite.routes import Get
from app.resources.CountryResource import CountryResource
from app.resources.AfricaResource import AfricaResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get('/api', 'AfricaDataController@show').name('api'),
    Get('/api/africa/countries/@country',
        'AfricaCountryController@single').name('country'),
    Get('api/africa/date/@date', 'AfricaDataController@single').name('date'),
    Get('/api/africa/hist/@country', 'CountryHistoricController@single'),
    # Api Routes
    CountryResource('/api/africa/countries').routes(),

    AfricaResource('/api/africa').routes(),
]
