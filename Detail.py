import get_datas


class Detail:
    def __init__ (self, name, material, thicknes, dimmensions, cut_time, quantity, price = 0):
        self.name = name
        self.material = material
        self.thicknes = thicknes
        self.dimmensions = dimmensions
        self.cut_time = cut_time
        self.quantity = quantity
        self.price = 0

