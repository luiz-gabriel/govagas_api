from Models.RegisterJob import Register

class InsertJob:

    def run(data):
        data['slug'] = Register.generateSlug(data['title'])
        return Register.reg(data)