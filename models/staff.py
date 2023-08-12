from odoo import models, fields

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This is the model for our staff"

    name = fields.Char(string="Name", size=50)
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")