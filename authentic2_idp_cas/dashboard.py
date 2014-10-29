from admin_tools.dashboard import modules

def get_admin_modules():
    '''Show Client model in authentic2 admin'''
    model_list = modules.ModelList('CAS',
            models=('authentic2_idp_cas.models.CasService',
                    'authentic2_idp_cas.models.CasTicket'
                    ))
    return (model_list,)
