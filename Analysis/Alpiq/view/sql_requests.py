data_query = """
    select distinct
        i.start_date,
        i.direction,
        i.resource,
        i.alert,
        i.downgraded,
        a.value as available_value,
        r.value as required_value,
        a.value/r.value * 1000 as ratio,
        
        prfcr.value as procured_fcr,
        actofcr.value as activated_fcr,
        accofcr.value as accepted_fcr,
        
        prafrr.value as procured_afrr,
        actoafrr.value as activated_afrr,
        accoafrr.value as accepted_afrr,
        
        prm.value as procured_mfrr,
        actom.value as activated_mfrr,
        accom.value as accepted_mfrr,
        
        prrr.value as procured_rr,
        actorr.value as activated_rr,
        accorr.value as accepted_rr
    from 
        table_df as i
        
        
    left join
        (select * from table_df as t where t.resource = 'peak_daily_margins' and t.value_type = 'required_value') as r
            on i.start_date = r.start_date
    left join
        (select * from table_df as t where t.resource = 'peak_daily_margins' and t.value_type = 'available_value') as a
            on i.start_date = a.start_date
            
            
    left join
        (select * from table_df as t where t.resource = 'procured_reserves' and t.value_type = 'value' and t.type='FCR' and t.direction = '{procured_direction}') as prfcr
            on i.start_date = prfcr.start_date
    left join
        (select * from table_df as t where t.resource = 'activated_offers' and t.value_type = 'value' and t.type='FCR' and t.direction = '{activated_direction}') as actofcr
            on i.start_date = actofcr.start_date
    left join
        (select * from table_df as t where t.resource = 'accepted_offers' and t.value_type = 'value' and t.type='FCR' and t.direction = '{accepted_direction}') as accofcr
            on i.start_date = accofcr.start_date
            
            
    left join
        (select * from table_df as t where t.resource = 'procured_reserves' and t.value_type = 'value' and t.type='AFRR' and t.direction = '{procured_direction}') as prafrr
            on i.start_date = prafrr.start_date
    left join
        (select * from table_df as t where t.resource = 'activated_offers' and t.value_type = 'value' and t.type='aFRR' and t.direction = '{activated_direction}') as actoafrr
            on i.start_date = actoafrr.start_date
    left join
        (select * from table_df as t where t.resource = 'accepted_offers' and t.value_type = 'value' and t.type='AFRR' and t.direction = '{accepted_direction}') as accoafrr
            on i.start_date = accoafrr.start_date
    
    
    left join
        (select * from table_df as t where t.resource = 'procured_reserves' and t.value_type = 'value' and t.type='MFRR' and t.direction = '{procured_direction}') as prm
            on i.start_date = prm.start_date
    left join
        (select * from table_df as t where t.resource = 'activated_offers' and t.value_type = 'value' and t.type='mFRR' and t.direction = '{activated_direction}') as actom
            on i.start_date = actom.start_date
    left join
        (select * from table_df as t where t.resource = 'accepted_offers' and t.value_type = 'value' and t.type='MFRR' and t.direction = '{accepted_direction}') as accom
            on i.start_date = accom.start_date
            
            
    left join
        (select * from table_df as t where t.resource = 'procured_reserves' and t.value_type = 'value' and t.type='RR' and t.direction = '{procured_direction}') as prrr
            on i.start_date = prrr.start_date
    left join
        (select * from table_df as t where t.resource = 'activated_offers' and t.value_type = 'value' and t.type='RR' and t.direction = '{activated_direction}') as actorr
            on i.start_date = actorr.start_date
    left join
        (select * from table_df as t where t.resource = 'accepted_offers' and t.value_type = 'value' and t.type='RR' and t.direction = '{accepted_direction}') as accorr
            on i.start_date = accorr.start_date
    where
        i.downgraded in ({downgraded}) and
        i.resource = 'accepted_offers' and 
        i.value_type = 'value' and
        i.type = 'FCR';
"""

MA_query = """
    select distinct
        i.start_date,
        i.direction,
        i.resource,
        i.alert,
        i.downgraded,
        a.value as peak_available_value,
        r.value as peak_required_value,
        
        prm.value as procured_mfrr,
        actom.value as activated_mfrr,
        accom.value as accepted_mfrr,
        
        prrr.value as procured_rr,
        actorr.value as activated_rr,
        accorr.value as accepted_rr,
        
        case cast (strftime('%w', i.start_date) as integer)
          when 0 then 'Sunday'
          when 1 then 'Monday'
          when 2 then 'Tuesday'
          when 3 then 'Wednesday'
          when 4 then 'Thursday'
          when 5 then 'Friday'
          else 'Saturday' end as weekday
    from 
        table_df as i
        
        
    left join
        (select * from table_df as t where t.resource = 'peak_daily_margins' and t.value_type = 'required_value') as r
            on i.start_date = r.start_date
    left join
        (select * from table_df as t where t.resource = 'peak_daily_margins' and t.value_type = 'available_value') as a
            on i.start_date = a.start_date
         
    left join
        (select * from table_df as t where t.resource = 'procured_reserves' and t.value_type = 'value' and t.type='MFRR' and t.direction = '{procured_direction}') as prm
            on i.start_date = prm.start_date
    left join
        (select * from table_df as t where t.resource = 'activated_offers' and t.value_type = 'value' and t.type='mFRR' and t.direction = '{activated_direction}') as actom
            on i.start_date = actom.start_date
    left join
        (select * from table_df as t where t.resource = 'accepted_offers' and t.value_type = 'value' and t.type='MFRR' and t.direction = '{accepted_direction}') as accom
            on i.start_date = accom.start_date
            
            
    left join
        (select * from table_df as t where t.resource = 'procured_reserves' and t.value_type = 'value' and t.type='RR' and t.direction = '{procured_direction}') as prrr
            on i.start_date = prrr.start_date
    left join
        (select * from table_df as t where t.resource = 'activated_offers' and t.value_type = 'value' and t.type='RR' and t.direction = '{activated_direction}') as actorr
            on i.start_date = actorr.start_date
    left join
        (select * from table_df as t where t.resource = 'accepted_offers' and t.value_type = 'value' and t.type='RR' and t.direction = '{accepted_direction}') as accorr
            on i.start_date = accorr.start_date
    where
        i.downgraded in ({downgraded}) and
        i.resource = 'accepted_offers' and 
        i.value_type = 'value' and
        i.type = 'FCR';
"""

weekday_query = """
    select distinct
        t.start_date,
        t.resource,
        t.type,
        t.direction,
        t.downgraded,
        t.alert,
        t.value as {value_type},
        case cast (strftime('%w', t.start_date) as integer)
          when 0 then 'Sunday'
          when 1 then 'Monday'
          when 2 then 'Tuesday'
          when 3 then 'Wednesday'
          when 4 then 'Thursday'
          when 5 then 'Friday'
          else 'Saturday' end as weekday
        
        
    from 
        {table_df} as t
    where
        t.resource = '{resource}' and
        t.value_type = '{value_type}';
    
"""

direction_query = """
    select distinct
        i.start_date,
        i.direction,
        i.resource,
        i.alert,
        i.downgraded,
        
        up.value as {resource}_{resource_type}_UPWARD,
        down.value as {resource}_{resource_type}_DOWNWARD,
        flat.value as {resource}_{resource_type}_UP_DOWN,
        
        
        
    from 
        table_df as i
                 
    left join
        (select * from table_df as t where t.resource = '{resource}' and t.value_type = '{value_type}' and t.type='{resource_type}' and t.direction = 'UPWARD') as up
            on i.start_date = up.start_date
    left join
        (select * from table_df as t where t.resource = '{resource}' and t.value_type = '{value_type}' and t.type='{resource_type}' and t.direction = 'DOWNWARD') as down
            on i.start_date = down.start_date
    left join
        (select * from table_df as t where t.resource = '{resource}' and t.value_type = '{value_type}' and t.type='{resource_type}' and t.direction = 'UP_DOWN') as flat
            on i.start_date = flat.start_date
            
    where
        i.downgraded in ({downgraded}) and
        i.resource = 'accepted_offers' and 
        i.value_type = 'value' and
        i.type = 'FCR';
"""