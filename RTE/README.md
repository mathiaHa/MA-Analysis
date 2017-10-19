# Explications Données RTE
Référence les liens des explications de RTE en fonction des noms de ressources utilisées

## [Equilibrage](https://github.com/mathiaHa/MA-Analysis/tree/rteb/RTE/RTEData/rte_data_samples/Equilibrage)

### [Balancing Capacity](https://github.com/mathiaHa/MA-Analysis/tree/rteb/RTE/RTEData/rte_data_samples/Equilibrage/balancing_capacity)

* [procured_reserves](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/reserve_ajustement.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_capacity/procured_reserves.json)
* [accepted_offeres](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/volume_journalier_energie_ajustement.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_capacity/accepted_offers.json)
* [insufficients_offers](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/histo/modesDegrades.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_capacity/insufficients_offers.json)
* [peak_daily_margins](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/jour/marges.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_capacity/peak_daily_margins.json)  
La forme de la courbe de consommation évolue au cours de l'année, en été il n'existe plus de pointe de consommation le soir : la marge associée n'est donc plus calculée.

### [Balancing Energy](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/volumes_prix/equilibrage.jsp)

> [Les examples issues de la page test des apis sont faux.](./RTEData/rte_data_samples/Equilibrage/balancing_energy)  
> Il faut donc se rendre sur le [guide explicatif de l'API](https://data.rte-france.com/documents/20182/33858/user_guide/a6c21922-a2f6-4a05-83a9-b727f47dafa2?version=1.0) et lire chaque description/exemple.

* [capacities_prices]()
* [imbalance_data](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/volumes_prix/pre.jsp)-> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_energy/imbalance_data.json)
* [lead_times](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/volumes_prix/DMO_Domin.jsp)-> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_energy/lead_times.json)
* [prices](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/jour/courbe.jsp)-> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_energy/prices.json)
* [tso_offers](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/echanges_entre_GRT_PS_histo.jsp)-> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_energy/tso_offers.json)  
> Représente le système d'[échange Balit](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/echanges_balit.jsp) entre GRT
* [volumes_per_reasons](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/volumes_prix/motif.jsp)-> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_energy/volumes_per_reasons.json)
* [volumes_per_energy_type](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/mecanisme/volumes_prix/type_offre.jsp)-> [Sample](./RTEData/rte_data_samples/Equilibrage/balancing_energy/volumes_per_energy_type.json)

### [Bre temporal reconstitution](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/vie_reconst_flux.jsp)


> national_reference_load_curves - national_measured_by_RE_load_curves = national_profiling_imbalances  
> Quand national_profiling_imbalances < 0 on a national_alignment_coefficients < 1  
> Donc national_alignment_coefficients = national_reference_load_curves / national_measured_by_RE_load_curves  

* [national_reference_load_curves](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/vie_reconst_flux_C10.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/bre_imbalance_reconstitution/national_reference_load_curves.json)
* [national_profiling_imbalances](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/vie_reconst_flux_C11.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/bre_imbalance_reconstitution/national_profiling_imbalances.json)
* [national_alignment_coefficients](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/vie_reconst_flux_C12.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/bre_imbalance_reconstitution/national_alignment_coefficients.json)
* [additional_national_alignment_coefficients](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/vie_reconst_flux_C41.jsp) -> [Sample](./RTEData/rte_data_samples/Equilibrage/bre_imbalance_reconstitution/additional_national_alignment_coefficients.json)

#### --> contient: Bre temporal reconciliations

## [Mécanisme de Capacité](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/meca_capa/meca_capa.jsp)

### [signal](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/meca_capa/meca_capa_pp.jsp)
[Sample](./RTEData/rte_data_samples/Mecanisme_Capacite/signal/signals.json)

## [Production](https://github.com/mathiaHa/MA-Analysis/tree/rteb/RTE/RTEData/rte_data_samples/Production)

### [Generation_forast](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/prevision_production.jsp)

### [Unavailability additional information](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/indisponibilites.jsp)

* [generation_unavailabilities](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/indisponibilites.jsp)
* [transmission_network_unavailabilities](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/PMD_hebdo.jsp)

### Generation installed capacities

* [capacities_cpc](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/parc_reference.jsp)
* [capacities_per_production_type](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/realisation_production.jsp)
* [capacities_per_production_unit](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/prod/production_groupe.jsp)


## Non classé mais intéressants
* [Nom-code EIC du RE](http://clients.rte-france.com/lang/fr/clients_traders_fournisseurs/vie/meca_capa/meca_capa_rpc.jsp)