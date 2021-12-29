from connect_ import get_all_data 
from assets import Bike, Price_delta

def main(): 
    bikes = list()
    deltas = list()
    listings, price_changes = get_all_data()            # stores a list of dictionaries, each dict has the info for 1 item 
    for listing in listings:
        try: 
            bikes.append(Bike(listing)) 
        except KeyError:                    # If we couldn't create an object properly, it probably isn't a bike ad (it's missing a key in the dict), skip it
            pass
    for price_change in price_changes:  
        deltas.append(Price_delta(price_change))        # creating list of bike objects and price changes 
    print(len(bikes), len(deltas)) # TODO: returning 0, 31255 --> we are having problems with bike list creation after update 
    for delta_obj in deltas:
        ad_id_delta = delta_obj.return_main_id()    
        for bike_obj in bikes:
            if ad_id_delta == bike_obj.return_main_id(): 
                bike_obj.price_deltas.append(delta_obj) 
                print("passed") 
    for bike_obj in bikes: 
        if bike_obj.price_deltas != []:
            print(bike_obj.price_deltas)
        #TODO get bike object corresponding to delta 

if __name__ == '__main__':
    main() 
    

