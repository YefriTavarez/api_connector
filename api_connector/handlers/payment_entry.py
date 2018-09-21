# -*- coding: utf-8 -*-
# Copyright (c) 2018, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe

from api_connector import logger

def execute(doc, event):
	conf = frappe.get_single("API Conf")

	response = conf.post_request(doc.as_json())

	if response.status_code == 200:
		logger.write_info_log(doc.doctype, doc.as_json())
	else:
		logger.write_error_log(doc.doctype, doc.as_json())
