# XXX: does not represent None as null, rather as '...\n'
from .type_checks import dt_check_isinstance


def yaml_load(s: str):
    dt_check_isinstance("s", s, str)
    from ruamel.yaml import YAML

    if s.startswith("..."):
        return None
    try:
        l = YAML(typ="rt").load(s)
    except:
        l = YAML(typ="unsafe").load(s)

    return dict(l)


def yaml_load_plain(s: str):
    dt_check_isinstance("s", s, str)
    from ruamel.yaml import YAML

    if s.startswith("..."):
        return None
    l = YAML(typ="unsafe").load(s)
    # return remove_unicode(l)
    return dict(l)


def yaml_dump(s) -> str:
    from ruamel.yaml import YAML
    from ruamel.yaml.compat import StringIO

    d = YAML(typ="rt")
    d.allow_unicode = False
    stream = StringIO()
    d.dump(s, stream)
    return stream.getvalue()


def yaml_dump_pretty(ob) -> str:
    from ruamel.yaml import YAML
    from ruamel.yaml.compat import StringIO

    d = YAML(typ="rt")
    d.allow_unicode = False
    stream = StringIO()
    d.dump(ob, stream)
    return stream.getvalue()
