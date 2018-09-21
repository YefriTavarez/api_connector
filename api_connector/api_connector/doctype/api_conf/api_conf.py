# -*- coding: utf-8 -*-
# Copyright (c) 2018, Yefri Tavarez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe import _
from frappe.model.document import Document

from api_connector.client import Client

class APIConf(Document):
	def __init__(self, *args, **kwargs):
		super(APIConf, self).__init__(*args, **kwargs)

		self.set("client", Client(self.url, self.username, self.get_password()))

	def get_request(self, params):
		client = self.get("client")

		if not client: return

		return client.__post__(self.url, params)

	def post_request(self, data):
		client = self.get("client")

		if not client: return

		return client.__post__(self.url, data)

	def validate(self):
		client = self.get("client")

		if not client: return

		response = client.__post__(self.url, { "data": "validate" })

		if not response.status_code == 200:
			frappe.throw(_("Invalid API Login!"))
	
