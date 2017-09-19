### [MAIN DESIGN](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/Main_design.pdf)
Pour les ressources:
* RTE-Equilibrage-
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
* RTE-Interconnexion:
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
* RTE-Mecanisme_capacite:
	* registry_consumption_controles_measures:
		 * registry_consumption_controles_measures
	* signal:
		* signals
* RTE-Production:
	* actual_generation:
		* actual_generations_per_production_type
		* actual_generations_per_unit
		* generation_mix_15min_time_scale
		* water_reserves
	* generation_forecast
		* forecasts
* RTE-Production:
	* generation_installed_capacities:
		* capacities_per_production_type
		* capacities_per_production_unit
	* unavailability_additional_information
		* generation_unavailabilities
		* transmission_network_unavailabilities
	* wholesale_market
		* epex_spot_power_exchanges
* RTE-Consommation:
	* tempo_like_supply_contract
		* tempo_like_calendars
	
### [MAIN DESIGN WITH CONDITION](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/RTE-Equilibrage-Balancing_energy.pdf)

Pour les ressources:
* RTE-Equilibrage
	* balancing_energy:
	    * imbalance_data
	    * lead_times
	    * prices
	    * tso_offers
	    * volumes_per_energy
	    * volumes_per_entity
	    * volumes_per_reasons
	
### [SINGLE LAYER DESIGN](https://github.com/mathiaHa/MA-Analysis/blob/master/RTEData/single_layer_design.pdf)
Pour les ressources:
* RTE-Interconnexion:
	* congestion:
		* costs
* RTE-Mecanisme_capacite:
	* certified_capacities_registry:
		* ncc_greater_equal_100_mw
		* ncc_less_100_mw
* RTE-Production:
	* generation_installed_capacities:
		* capacities_cpc
	


	
