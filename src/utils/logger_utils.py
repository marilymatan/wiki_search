from connexion.apps.flask_app import logger
from functools import wraps


def get_params_string(params, divider):
    return divider.join("{}: {}".format(*param) for param in params.items())


def log_endpoint(endpoint_name, key='args_data'):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if logger.root.level == 10:
                if key in kwargs:
                    # POST method
                    params_string = get_params_string(kwargs[key], divider=' | ')
                else:
                    # GET method
                    params_string = get_params_string(kwargs, divider=' | ')
                if not params_string:
                    log_string = f'{endpoint_name} ({f.__name__} - no params)'
                else:
                    log_string = f'{endpoint_name} ({f.__name__}) - [params] - {params_string}'
                logger.info(log_string)
            return f(*args, **kwargs)
        return wrapper
    return decorator
