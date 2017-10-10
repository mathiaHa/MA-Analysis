#!/usr/bin/python
# -*- coding: utf-8 -*-

# Normalization of CSV
titles =  ["type", "direction", "value", "price"]
columns = ["Heures"] + titles

traduction ={
    "Réserve primaire" : "FCR",
    "Réserve secondaire" : "aFRR",
    "Réserve rapide": "mFRR",
    "Réserve complémentaire": "RR",
    
    "A la hausse et à la baisse" : "UP_DOWN",
    "A la hausse" : "UPWARD",
    "A la baisse" : "DOWNWARD"
}

separators = ["\t", ";", ",", " "]

# Model of data for cosmosDB
document_model = {
    "actionid": None,
    "actiontype": "rte",
    "actioncollection": "scheduler",
    "resourcename": "activated_offers",
    "apiname": "balancing_capacity",
    "start_date": "2014-12-18T00:00:00+01:00",
    "end_date": "2014-12-19T00:00:00+01:00",
    "data": []
}