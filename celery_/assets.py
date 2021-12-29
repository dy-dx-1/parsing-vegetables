class Connect:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password 
        self.host = host
        self.port = port 
        self.database = database 
    def return_info(self):
        info = (self.user, self.password, self.host, self.port, self.database) 
        return info 

class Bike: 
    price_deltas = [] # This empty list will contain the price delta objects associated to a particular bike after update 

    def __init__(self, listing):
        self.ad_id = int(listing['ad_id']) 
        self.price = float(listing['price'])
        self.description = listing['description']
        self.pictures = listing['pictures']
        self.url = listing['url'] 
        self.location = listing['location']
        self.model = listing['model']
        self.year = listing['year']
        self.groupset = listing['groupset']
        self.bike_type = listing['bike_type']
        self.date = listing['date']
        self.title = listing['title']
        self.active = True if listing['active'] == 'active' else False 
        self.inactive_date = listing['inactive_date']

    def return_imp_info(self):
        return self.ad_id, self.price, self.active 

    def return_main_id(self):                              #Taking price_delta object and checking if an ad id corresponds to the bike
        return self.ad_id    # NOTE: this is for a single ad dict, so we have to use a for loop in main 


class Price_delta: 
    def __init__(self, price_info): 
        self.change_id = price_info['change_id'] 
        self.ad_id = int(price_info['ad_id']) 
        self.price_before = float(price_info['price_before'])
        self.price_after = float(price_info['price_after'])
        self.delta_price = float(price_info['change_diff'])
        self.date = price_info['date'] 
    def return_imp_info(self):
        return self.ad_id, self.price_before, self.price_after 
    def return_main_id(self):
        return self.ad_id

    





