class settings:
    host = "https://localhost:8081"
    master_key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
    database_id = "LaSD"
    scheduler_id = "scheduler_causality1"
    errors_id = "errors"
    collection_id = "rte4"

class groups:
    balancing_capacity = "type"
    balancing_energy = "tso_offering"
    bre_imbalance_reconstitution = None
    bre_temporal_reconciliations = "type"
    
    actual_generation = "production_type"
    generation_forecast = "type"
    generation_installed_capacities = "type"
    unavailability_additional_information = "type"
    wholesale_market = None
    

class rteapi:
    def __init__(self):
        self.balancing_capacity = ["accepted_offers", "insufficients_offers", "peak_daily_margins", "procured_reserves"]
        self.balancing_energy = ["capacities_prices", "imbalance_data", "lead_times", "prices", "tso_offers", "volumes_per_reasons", "volumes_per_entity_type", "volumes_per_energy_type"]
        self.signals = ["signal"]
    
    def findapi( self, resource ):
        for property, resources in self.__dict__.iteritems():
            print property
            if resource in resources:
                return property
        return "not found"