# -*- coding: utf-8 -*-
# Copyright (c) 2018, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe import _
from requests import Session

class Client:
	def __init__(self, url, username, password):
		self.username = username
		self.password = password

		response = self.session.get(url, auth=(username, password))

		if not "NULL" in response.text:
			frappe.throw(_("Invalid login info!"))

	def __get__(self, url, params):
		return self.session.get(url, auth=(self.username, self.password), params=params)

	def __post__(self, url, data):
		return self.session.post(url, auth=(self.username, self.password), data=data)

	session = Session()
