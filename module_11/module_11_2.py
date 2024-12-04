import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому объект принадлежит
    module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    # Получаем другие интересные свойства объекта, учитывая его тип
    additional_info = {}
    if inspect.isclass(obj):
        additional_info['bases'] = [base.__name__ for base in obj.__bases__]
        additional_info['mro'] = [cls.__name__ for cls in inspect.getmro(obj)]
    elif inspect.isfunction(obj) or inspect.ismethod(obj):
        additional_info['signature'] = str(inspect.signature(obj))
        additional_info['docstring'] = inspect.getdoc(obj)
    elif inspect.ismodule(obj):
        additional_info['file'] = inspect.getfile(obj) if hasattr(obj, '__file__') else None
        additional_info['docstring'] = inspect.getdoc(obj)

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'additional_info': additional_info
    }


# Пример использования
number_info = introspection_info(42)
print(number_info)

