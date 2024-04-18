
def pop_from_data(pop_list, data) -> dict:
    """
    Removes useless data in provided data dict
    """
    
    for _ in pop_list:
        if _ in data:
            data.pop(_)
    return data


def request_from_args(args):
    """
    Extract `request`
    condition applied as first param to a view can be `self`
    """
    
    try:
        return args[1]
    except:
        return args[0]


def id_from_query_params_or_body(request, lookup_key=None):
    """
    Fecth id from query_param or body
    """
    
    if not lookup_key:
        lookup_key = "id"

    if request.query_params.get(lookup_key, 0):
        return request.query_params.get(lookup_key, 0)
    else:
        return request.data.get(lookup_key, 0)