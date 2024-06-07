# -*- coding: utf-8 -*-

log_config ={
  'version': 1,
  'formatters': {
    'success_formatter': {
      'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    },
    'bad_formatter': {
      'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    },
    'blocked_formatter': {
      'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    },
  },
  'handlers': {
    'success_handler': {
      'class': 'logging.FileHandler',
      'formatter': 'success_formatter',
      'filename': 'success.log',
      'encoding': 'utf-8',
    },
    'bad_handler': {
      'class': 'logging.fileHandler',
      'formatter': 'bad_formatter',
      'filename': 'bad.log',
      'encoding': 'utf-8',
    },
    'blocked_handler': {
      'class': 'logging.FileHandler',
      'formatter': 'blocked_formatter',
      'filename': 'blocked.log',
      'encoding': 'utf-8',
    },
  },
  'loggers': {
    'success': {
      'handlers': ['success_handler'],
      'level': 'INFO',
    },
    'bad': {
      'handlers': ['bad_handler'],
      'level': 'WARNING',
    },
    'blocked': {
      'handlers': ['blocked_handler'],
      'level': 'ERROR',
    },
  },
}