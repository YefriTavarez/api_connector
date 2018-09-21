import frappe, os

from frappe import scrub
from frappe.utils import cstr


def write_info_log(doctype, data):
	"""
	Writes data into the log file
	"""
	filename = get_file_name(doctype, state="info_")

	with open(filename, 'a') as log:
		log.write(cstr(data))

	log.close()

def write_error_log(doctype, data):
	"""
	Writes data into the error log file
	"""
	filename = get_file_name(doctype, state="error_")

	with open(filename, 'a') as log:
		log.write(cstr(data))

	log.close()

def get_file_name(doctype, state=""):
	"""
	Returns the filename and path for logging purposes given the doctype
	:param doctype: DocType involved
	"""

	today = frappe.utils.nowdate()
	pathname = "logs/{0}".format(scrub(doctype))

	frappe.create_folder(pathname)

	return "{pathname}/{doctype}_sync_{state}{date}.log".format(date=scrub(today),
		pathname=pathname, state=state, doctype=scrub(doctype))
