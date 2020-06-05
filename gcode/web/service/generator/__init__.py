from .generator import Generator
import  os
import  importlib
generator_map={}

def init():
    for p, f, file_list in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), os.curdir))):
        for _file in file_list:
            arr = _file.split(".")
            file_name = arr[0]
            file_type = arr[1]
            if file_type == "py" and file_name != "__init__" and file_name != "generator":
                importlib.import_module("."+file_name,package=__name__)
    generator_map[Generator.__name__] = {"code": Generator.__name__, "name": Generator.__name__, "object": Generator()}
    for cl in Generator.__subclasses__():
        obj = cl()
        generator_map[cl.__name__]={"code":cl.__name__,"name":cl.__name__,"object":obj}
    pass
init()
