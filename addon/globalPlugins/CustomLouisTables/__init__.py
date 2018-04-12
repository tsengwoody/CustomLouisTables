# coding: utf-8
# CustomLouisTables:
# Copyright (C) 2018 Tseng Woody <tsengwoody.tw@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import inspect
import os
import shutil
import sys


import config
import globalPluginHandler
import globalVars
import ui
import braille
import braille_custom

origin_regions = {i: getattr(braille, i) for i in dir(braille) if inspect.isclass(getattr(braille, i)) and issubclass(getattr(braille, i), braille.Region) }
custom_regions = {i: getattr(braille_custom, i) for i in dir(braille_custom) if inspect.isclass(getattr(braille_custom, i)) and issubclass(getattr(braille_custom, i), braille_custom.Region) }

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("CustomLouisTables")

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)

		try:
			config.conf["CustomLouisTables"]["toggle"]
		except:
			config.conf["CustomLouisTables"] = {}
			config.conf["CustomLouisTables"]["toggle"] = "On"

		if config.conf["CustomLouisTables"]["toggle"] == "On":
			for key, value in custom_regions.items():
				setattr(braille, key, value)
		else:
			for key, value in origin_regions.items():
				setattr(braille, key, value)

	def script_toggle(self, gesture):

		try:
			config.conf["CustomLouisTables"]["toggle"]
		except:
			config.conf["CustomLouisTables"] = {}
			config.conf["CustomLouisTables"]["toggle"] = "On"

		if config.conf["CustomLouisTables"]["toggle"] == "On":
			for key, value in origin_regions.items():
				setattr(braille, key, value)
			config.conf["CustomLouisTables"]["toggle"] = "Off"
		else:
			for key, value in custom_regions.items():
				setattr(braille, key, value)
			config.conf["CustomLouisTables"]["toggle"] = "On"
		ui.message(config.conf["CustomLouisTables"]["toggle"])
	script_toggle.category = scriptCategory
	# Translators: message presented in input mode.
	script_toggle.__doc__ = _("Toggle CustomLouisTables")
