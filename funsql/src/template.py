"""
sql templates!
"""

__all__ = ["readTemplates"]

import re
from importlib.resources import files
from .pghook import Hook

red = "\x1b[31m{}\x1b[0m".format
blue= "\x1b[34m{}\x1b[0m".format
# Example: print(f"Hello {red('blue')}")


words = files('funsql').joinpath('data/sql_keywords.txt').read_text().splitlines()


# Example: template.setFormat('{One} {Two}').replaceParam()
# getattr(template.setFormat('{One} {Two}'),'replaceParam')()
class setFormat(str):
    def __init__(self,s):
        self.s = s
    def replaceParam(self,*args,**kwargs):
        s = self.s
        pa = re.findall('{\s?(.+?)\s?}', s)
        argss = list(args)
        param = {}
        for p in pa:
            if p not in param.keys():
                if p in kwargs.keys():
                    param[p] = kwargs.pop(p)
                elif argss:
                    param[p] = argss.pop(0)
                else:
                    param[p] = '{'+p+'}'
#         if kwargs or argss:
#             print(red(str(kwargs)+str(argss))+ ' not used')
        return setQueries(s.format(**param))

# Define methodes available to templates
class setQueries(str):
    def __init__(self,q):
        self.q = q    

    def __call__(self):
        return Hook().get(self.q)

    def __add__(self,other):
        return setQueries(self.q +"\n"+ other)

    def __repr__(self):
        ss = self.q
        # color keywords
        for w in words:
            insensitive_word = re.compile(r"\b" + re.escape(w)+ r"\b", re.IGNORECASE)
            ss = insensitive_word.sub(blue(w), ss)
        # color comments
        ss = re.compile("/\*").sub("\x1b[32m/*", ss)  
        ss = re.compile("\*/").sub("*/\x1b[0m", ss)
        return ss
    
# access templates with "."
# https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = setFormat(v).replaceParam
                    
        if kwargs:
            for k, v in kwargs.items():
                self[k] = setFormat(v).replaceParam

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]
        
# read templates
def readTemplates(filename):
    templates = {}
    key = None
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if line.startswith("-->"):
                key = re.search(r'--> (.*?)\n',line).group(1).strip()
            elif line.startswith("--") or line.strip()=="":
                None
            else:
                if key in templates.keys():
                    templates[key]= templates[key] + line
                else:
                    templates[key] = line
    return Map(templates)

# # add static queries
# # Does not get variable
# s['new'] = template.setQueries('select 1')
# s.new.get()

# # add dynamic queries
# s['dynamic'] = template.setFormat('select {num}').replaceParam
# s.dynamic(3).get()