from connect_ import get_all_data 
from assets import Bike, Price_delta

def main(): 
    bikes = list()
    deltas = list()
    listings, price_changes = get_all_data()            # stores a list of dictionaries, each dict has the info for 1 item 

    for listing in listings:
        bikes.append(Bike(listing)) 
    for price_change in price_changes:  
        deltas.append(Price_delta(price_change))        # creating list of bike objects and price changes 

    all_ids = [] 
    for bike_obj in bikes:
        all_ids.append(bike_obj.return_main_id())       # now we have a list of all the ids for each bike ad 
    for delta_obj in deltas:
        ad_id_delta = delta_obj.return_main_id()    
        if ad_id_delta in all_ids:
            print("eyy") 

if __name__ == '__main__':
    main() 
    

