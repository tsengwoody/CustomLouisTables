# coding: utf-8
# CustomLouisTables:
# Copyright (C) 2018 Tseng Woody <tsengwoody.tw@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import inspect

import config
import globalPluginHandler
import louis
import ui

from decorator import customTableList

origin_translate = louis.translate
origin_translateString = louis.translateString
origin_backTranslate = louis.backTranslate
origin_backTranslateString = louis.backTranslateString

custom_translate = customTableList(louis.translate)
custom_translateString = customTableList(louis.translateString)
custom_backTranslate = customTableList(louis.backTranslate)
custom_backTranslateString = customTableList(louis.backTranslateString)

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
			louis.translate = custom_translate
			louis.translateString = custom_translateString
			louis.backTranslate = custom_backTranslate
			louis.backTranslateString = custom_backTranslateString
		else:
			louis.translate = origin_translate
			louis.translateString = origin_translateString
			louis.backTranslate = origin_backTranslate
			louis.backTranslateString = origin_backTranslateString

	def script_toggle(self, gesture):

		try:
			config.conf["CustomLouisTables"]["toggle"]
		except:
			config.conf["CustomLouisTables"] = {}
			config.conf["CustomLouisTables"]["toggle"] = "On"

		if config.conf["CustomLouisTables"]["toggle"] == "On":
			louis.translate = origin_translate
			louis.translateString = origin_translateString
			louis.backTranslate = origin_backTranslate
			louis.backTranslateString = origin_backTranslateString
			config.conf["CustomLouisTables"]["toggle"] = "Off"
		else:
			louis.translate = custom_translate
			louis.translateString = custom_translateString
			louis.backTranslate = custom_backTranslate
			louis.backTranslateString = custom_backTranslateString
			config.conf["CustomLouisTables"]["toggle"] = "On"
		ui.message(config.conf["CustomLouisTables"]["toggle"])
	script_toggle.category = scriptCategory
	# Translators: message presented in input mode.
	script_toggle.__doc__ = _("Toggle CustomLouisTables")
