#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Part of coin_monitor. This is the logging module.
"""

VERSION = "V0.3 (2021-04-06)"

import sys
import os
sys.path.append('/home/chia/coin_monitor')
import yaml
import logging.config
import logging
import logging.handlers
import configparser
config = configparser.ConfigParser()

def setup_logging(default_path='/home/chia/coin_monitor/logging.yaml', default_level=logging.CRITICAL, env_key='LOG_CFG'):
    """Module to configure program-wide logging. Designed for yaml configuration files."""
    log_level = read_logging_config('coin_monitor_config', 'system_logging', 'log_level')
    log = logging.getLogger(__name__)
    level = logging._checkLevel(log_level)
    log.setLevel(level)
    system_logging = read_logging_config('coin_monitor_config', 'system_logging', 'logging')
    if system_logging:
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                try:
                    config = yaml.safe_load(f.read())
                    logging.config.dictConfig(config)
                except Exception as e:
                    print(e)
                    print('Error in Logging Configuration. Using default configs. Check File Permissions (for a start)!')
                    logging.basicConfig(level=default_level)
        else:
            logging.basicConfig(level=default_level)
            print('Failed to load configuration file. Using default configs')
            return log
    else:
        log.disabled = True


def read_logging_config(file, section, status):
    pathname = '/home/chia/coin_monitor/' + file
    config.read(pathname)
    if status == "logging":
        current_status = config.getboolean(section, status)
    else:
        current_status = config.get(section, status)
    return current_status


def main():
    print("This script is not intended to be run directly.")
    print("This is the systemwide logging module.")
    print("It is called by other modules.")
    exit()


if __name__ == '__main__':
    main()
