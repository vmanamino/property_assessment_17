
class Record():
    def __init__(self, data):
        self.pid = data['PID']
        self.address_one = 'none'
        if not data['MAIL_ADDRESS']:
            self.address_one = data['ST_NAME']
        else:
            self.address_one = data['MAIL_ADDRESS']
        self.address_zip = data['MAIL_ZIPCODE']
        self.address = self.address_one + ", "+self.address_zip.zfill(5)
        self.owner = data['OWNER']
        self.land_use = 'none'
        if (data['LU']):
            lu = data['LU']
            if lu == "A":
                self.land_use = 'Residential 7 or more units'
            if lu == "AH":
                self.land_use = 'Agricultural/Horticultural'
            if lu == "C":
                self.land_use = 'Commercial'
            if lu == "CC":
                self.land_use = 'Commercial condominium'
            if lu == "CD":
                self.land_use = 'Residential condominium'
            if lu == "CL":
                self.land_use = 'Commercial land'
            if lu == "CM":
                self.land_use = 'Condominium main'
            if lu == "CP":
                self.land_use = 'Condo parking'
            if lu == "E":
                self.land_use = 'Tax-exempt'
            if lu == "EA":
                self.land_use = 'Tax-exempt (121A)'
            if lu == "I":
                self.land_use = 'Industrial'
            if lu == "R1":
                self.land_use = 'Residential 1-family'
            if lu == "R2":
                self.land_use = 'Residential 2-family'
            if lu == "R3":
                self.land_use = 'Residential 3-family'
            if lu == "R4":
                self.land_use = 'Residential 4-family'
            if lu == "RC":
                self.land_use = 'Mixed use (res and comm)'
            if lu == "RL":
                self.land_use = 'Residential land'
        self.lot_size = data['LAND_SF']
        self.living_area = data['LIVING_AREA']
        self.land_value = data['AV_LAND']
        self.building_value = data['AV_BLDG']
        self.total_value = data['AV_TOTAL']
        