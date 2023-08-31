from pymongo.errors import ServerSelectionTimeoutError,ConfigurationError,ConnectionFailure



def error_handel(func):

    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print('Exiting Shell Net...')
        except (ConnectionError, ServerSelectionTimeoutError, ConfigurationError, ConnectionAbortedError, ConnectionFailure):
            print('Internet Connection Error. Try Again...')
        except TypeError:
            print('Invalid type to provide. Try Again...')    
            func(*args, **kwargs)
        except IndexError:
            print('Index out of range. Try Again...')
            func(*args, **kwargs)
        except Exception as e:
            print('Unknow error occured please try again.')
            print(e.with_traceback())
    return wrapper_func