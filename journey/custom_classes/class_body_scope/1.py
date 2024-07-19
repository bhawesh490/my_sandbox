class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = "{}.{}.{}".format(MAJOR, MINOR, REVISION)
    # since class variables are in the same scope we can directly refer them


# print(Language.FULL)


class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = "{}.{}.{}".format(MAJOR, MINOR, REVISION)

    @property
    def version(self):
        return "{}.{}.{}".format(self.MAJOR, self.MINOR, self.REVISION)

    @classmethod
    def cls_version(cls):
        return "{}.{}.{}".format(cls.MAJOR, cls.MINOR, cls.REVISION)

    @staticmethod
    def static_version():
        # this will not work as MAJOR, MINOR, REVISION are not in the global scope of module they
        # are in the class scope
        # return "{}.{}.{}".format(MAJOR, MINOR, REVISION)

        return "{}.{}.{}".format(Language.MAJOR, Language.MINOR, Language.REVISION)


l = Language()
print(l.version)
print(Language.cls_version())
print(Language.static_version())


class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 5


def full_version():
    return "{}.{}.{}".format(Language.MAJOR, Language.MINOR, Language.REVISION)


print(full_version())


class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 5
    version = full_version


print(Language.version())


MAJOR = 0
MINOR = 0
REVISION = 1


def gen_class():
    MAJOR = 0
    MINOR = 2
    REVISION = 4

    class Language:
        MAJOR = 3
        MINOR = 7
        REVISION = 4

        @classmethod
        def version(cls):
            return "{}.{}.{}".format(MAJOR, MINOR, REVISION)

        # now here attributes will get referred from the containing scope/clas with is the gen_class
        # major =3,minor =7 and revision = 4

    return Language


a = gen_class()
print(a.version())

import inspect

print(inspect.getclosurevars(a.version))
