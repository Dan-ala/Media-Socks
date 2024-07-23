class CustomerUserAdapter:
    def __init__(self, customer):
        self.customer = customer

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.customer.id)
