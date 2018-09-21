// Copyright (c) 2018, Yefri Tavarez and contributors
// For license information, please see license.txt

frappe.ui.form.on('API Conf', {
	"url": function(frm) {
		if (frm.doc.url) {
			frm.trigger("validate_url");
		}
	},
	"validate_url": function(frm) {
		if (!frappe.utils.validate_type(frm.doc.url, "url")) {
			frm.set_value("url", undefined);

			frappe.throw(__("Invalid URL format!"));
		}
	},
});
