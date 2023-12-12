from .models import SiteSetup


def site_setup(resquest):
    '''
    Realiza um consulta na base de dados SiteSetup de forma decrencente
    selecionnando a penas o primeiro registro.
    '''
    data = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': data
    }