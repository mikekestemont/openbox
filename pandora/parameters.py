#!usr/bin/env python
# -*- coding: utf-8 -*-

DEFAULT = 'default_settings.json'

import os
import json

class Settings(dict):

    def __init__(self, config_path=None):
        super(Settings, self).__init__()

        try:
            with open(config_path, 'r') as f:
                params = json.load(f)
        except:
            m = f'Could not read config file: {config_path}'
            raise ValueError(m)

        # add default values for missing settings:
        with open(os.sep.join((os.path.dirname(__file__),
                          'default_settings.json')), 'r') as f:
            defaults = json.load(f)

        for k in defaults:
            if k not in params:
                settings[k] = defaults[k]

        for k, v in params.items():
            self[k] = v

        # store the config path too:
        self.config_path = config_path

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Settings, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Settings, self).__delitem__(key)
        del self.__dict__[key]

    def __repr__(self):
        return 'Settings: ' + json.dumps(self, indent=4)

    def dump(self, path):
        with open(path, 'w') as f:
            json.dump(self, f, indent=4)

    @classmethod
    def load(self, path):
        s = Settings(path)
        return s

