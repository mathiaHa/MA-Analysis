# Structure de données venant de l'API de RTE

## 1. Explications

### 16/09/17
Choix de stockage des données sous formes de JSON.
Problèmes:
* L'API RTE, en fonction des ressources:
	* envoie des données structurées différement
	* possède des restrictions différentes
	* conseille une fréquences de mise à jour différente
* CosmosDB accepte des fichiers de taille limitée

### 25/09/17
Après relecture de certaines Ressources comme Interconnexion-Congestion-Costs, il me semble que les conseils "Préconisations d’appels
" correspondent à deux fréquences:
   * Fréquence de mise à jour des données
   * Fréquence du pas de temps pour chaque requête
	
## 2. Classements

Le nombre de couches est calculé entre la racine et chaques items de l'attribut "values" ou "time_series".
L'attribut de chaque ressource "nlayer" représente cette structure:
* single layer -> nlayer = 1
* two layers -> nlayer = 2
* two layers with condition -> nlayer = 21
* three layers -> nlayer = 3

### [MAIN DESIGN](./design/pdf/Main_design.pdf)
Pour les ressources:
* [RTE-Consommation](./rte_data_samples/Consommation):
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
* [RTE-Equilibrage](./rte_data_samples/Equilibrage):
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
* [RTE-Interconnexion](./rte_data_samples/Interconnexion):
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
* [RTE-Mecanisme_capacite](./rte_data_samples/Mecanisme_Capacite):
	* registry_consumption_controles_measures:
		 * registry_consumption_controles_measures
	* signal:
		* signals
* [RTE-Production](./rte_data_samples/Production):
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

### [MAIN DESIGN WITH CONDITION](./design/pdf/Condition_design.pdf)

Pour les ressources:
* [RTE-Equilibrage](./rte_data_samples/Equilibrage):
	* balancing_energy:
	    * imbalance_data
	    * lead_times
	    * prices
	    * tso_offers
	    * volumes_per_reasons
	    * volumes_per_energy_type
	    * volumes_per_entity_type
	
### [SINGLE LAYER DESIGN](./design/pdf/Single_layer_design.pdf)
Pour les ressources:
* [RTE-Consommation](./rte_data_samples/Consommation):
	* demand-response:
		* operators
* [RTE-Interconnexion](./rte_data_samples/Interconnexion):
	* congestion:
		* costs
* [RTE-Mecanisme_capacite](./rte_data_samples/Mecanisme_Capacite):
	* certified_capacities_registry:
		* ncc_greater_equal_100_mw
		* ncc_less_100_mw
* [RTE-Production](./rte_data_samples/Production):
	* generation_installed_capacities:
		* capacities_cpc

		
### [THREE LAYER DESIGN](./design/pdf/Tree_layer_design.pdf)
Pour les ressources:
* [RTE-Consommation](./rte_data_samples/Consommation):
	* big_adjusted
		* detailed


	
