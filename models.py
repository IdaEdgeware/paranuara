from marshmallow import Schema, fields, post_load

class Person(object):
    def __init__(self, person_name):
        self.person_name = name

class PersonSchema(Schema):
    person_name = fields.String()

    @post_load
    def create_person(self, data):
        return Person(**data)

class Company(object):
    def __init__(self, company_name):
        self.company_name = company_name

class CompanySchema(Schema):
    company_name = fields.String()

    @post_load
    def create_company(self, data):
        return Company(**data)
