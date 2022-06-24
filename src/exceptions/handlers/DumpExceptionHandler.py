import inspect
import os


def is_property(obj):
    return not inspect.ismethod(obj)


def is_local(obj_name, obj):
    return (
        not obj_name.startswith("__")
        and not obj_name.endswith("__")
        and not type(obj).__name__ == "builtin_function_or_method"
    )


def serialize_property(obj):
    if isinstance(obj, list):
        local_list = []
        for subobj in obj:
            local_list.append(serialize_property(subobj))
        return local_list
    elif isinstance(obj, dict):
        local_dict = {}
        for key, val in obj.items():
            local_dict.update({key: serialize_property(val)})
        return local_dict
    elif hasattr(obj, "serialize"):
        return obj.serialize()
    else:
        return str(obj)


class DumpExceptionHandler:
    def __init__(self, application):
        self.application = application

    def handle(self, exception):
        dumps = []
        # for dump in self.application.make("dumper").get_dumps():
        # for obj_name, obj in dump.objects.items():
        # all_members = inspect.getmembers(obj, predicate=inspect.ismethod)
        # all_properties = inspect.getmembers(obj, predicate=is_property)
        # members = {
        #     name: str(member)
        #     for name, member in all_members
        #     if is_local(name, member)
        # }
        # properties = {
        #     name: serialize_property(prop)
        #     for name, prop in all_properties
        #     if is_local(name, prop)
        # }
        # dumps.append(
        #     {
        #         "name": obj_name,
        #         "obj": str(obj),
        #         "members": members,
        #         "properties": properties,
        #     }
        # )
        dumps = self.application.make("dumper").get_serialized_dumps()
        
        import pdb
        pdb.set_trace()
