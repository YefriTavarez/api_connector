# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "api_connector"
app_title = "API Connector"
app_publisher = "Yefri Tavarez"
app_description = "An application to connect ERPNext with another system using basic auth"
app_icon = "octicon octicon-circuit-board"
app_color = "#356"
app_email = "yefritavarez@gmail.com"
app_license = "General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/api_connector/css/api_connector.css"
# app_include_js = "/assets/api_connector/js/api_connector.js"

# include js, css files in header of web template
# web_include_css = "/assets/api_connector/css/api_connector.css"
# web_include_js = "/assets/api_connector/js/api_connector.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "api_connector.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "api_connector.install.before_install"
# after_install = "api_connector.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "api_connector.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Customer": {
		"validate": "api_connector.handlers.customer.execute",
	},
	"Sales Invoice": {
		"validate": "api_connector.handlers.sales_invoice.execute",
	},
	"Payment Entry": {
		"validate": "api_connector.handlers.payment_entry.execute",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"api_connector.tasks.all"
# 	],
# 	"daily": [
# 		"api_connector.tasks.daily"
# 	],
# 	"hourly": [
# 		"api_connector.tasks.hourly"
# 	],
# 	"weekly": [
# 		"api_connector.tasks.weekly"
# 	]
# 	"monthly": [
# 		"api_connector.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "api_connector.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "api_connector.event.get_events"
# }

