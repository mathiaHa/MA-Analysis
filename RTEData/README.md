Le nombre de couches est calculé entre la racine et chaques items de l'attribut "values" ou "time_series".

### [MAIN DESIGN](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/Main_design.pdf)
Pour les ressources:
* [RTE-Consommation](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Consommation):
	* big_metering
		* validated_points
	* big_physical
		* validated_points
	* big_raw_metering
		* reference
	* big_system
		* validated_points
	* consolidated_consumption:
		* consolidated_energy_consumption
		* consolidated_power_consumption
	* consumption:
		* annual_forecasts
		* short_term
		* weekly_forecasts
	* demand-response:
		* volumes
	* id_referential:
		* getTarnscodification
	* speed_physical_view:
		* speed
	* speed_metering_view:
		* speed
	* tempo_like_supply_contract
		* tempo_like_calendars
* [RTE-Equilibrage](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Equilibrage):
	* balancing_capacity
		* accepted_offers
		* insufficients_offers
		* peak_daily_margins 
		* procured_reserves
	* bre_imbalance_reconstitution
		* additional_national_aligment_coefficients
		* procured_reserves
		* national_profiling_imbalances
		* national_reference_load_curves
	* bre_temporal_reconciliations
		* temporal_reconciliations
* [RTE-Interconnexion](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Interconnexion):
	* Congestion:
		* countertrading
		* redispatching
	* cross_zonal_capacity:
		* annual_monthly_auctions_specifications
		* initial_offered_capacities_d-1
		* initial_offered_capacities_id
		* results_id
	* exchange_schedule:
		* schedule
		* sum_rights_document
	* losses_publi_transmission_system
		* forecasts
	* ntc
		* ntc
	* physical_flow
		* physical_flows
* [RTE-Mecanisme_capacite](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Mecanisme_Capacite):
	* registry_consumption_controles_measures:
		 * registry_consumption_controles_measures
	* signal:
		* signals
* [RTE-Production](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Production):
	* actual_generation:
		* actual_generations_per_production_type
		* actual_generations_per_unit
		* generation_mix_15min_time_scale
		* water_reserves
	* generation_forecast
		* forecasts
	* generation_installed_capacities:
		* capacities_per_production_type
		* capacities_per_production_unit
	* unavailability_additional_information
		* generation_unavailabilities
		* transmission_network_unavailabilities
	* wholesale_market
		* epex_spot_power_exchanges

### [MAIN DESIGN WITH CONDITION](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/Condition_design.pdf)

Pour les ressources:
* [RTE-Equilibrage](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Equilibrage):
	* balancing_energy:
	    * imbalance_data
	    * lead_times
	    * prices
	    * tso_offers
	    * volumes_per_energy
	    * volumes_per_entity
	    * volumes_per_reasons
	
### [SINGLE LAYER DESIGN](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/Single_layer_design.pdf)
Pour les ressources:
* [RTE-Interconnexion](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Interconnexion):
	* congestion:
		* costs
* [RTE-Mecanisme_capacite](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Mecanisme_Capacite):
	* certified_capacities_registry:
		* ncc_greater_equal_100_mw
		* ncc_less_100_mw
* [RTE-Production](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Production):
	* generation_installed_capacities:
		* capacities_cpc
* [RTE-Consommation](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Consommation):
	* demand-response:
		* operators
		
### [THREE LAYER DESIGN](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/Tree_layer_design.pdf)
Pour les ressources:
* [RTE-Consommation](https://github.com/mathiaHa/MA-Analysis/tree/master/RTEData/rte_data_samples/Consommation):
	* big_adjusted
		* detailed


	
