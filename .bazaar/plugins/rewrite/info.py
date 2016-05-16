#!/usr/bin/python
from __future__ import absolute_import

bzr_plugin_name = 'rewrite'

bzr_plugin_version = (0, 6, 4, 'dev', 0)

bzr_compatible_versions = [(2, 5, 0), (2, 6, 0)]

bzr_minimum_version = bzr_compatible_versions[0]

bzr_maximum_version = bzr_compatible_versions[-1]

bzr_commands = [
    "pseudonyms",
    "replay",
    "rebase",
    "rebase_abort",
    "rebase_continue",
    "rebase_foreign",
    "rebase_todo",
    ]


