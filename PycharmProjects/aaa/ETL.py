subscriber_name=['Reliance','Airtel']
subscriber_id=['12542354','66644711']
target_systum=list(map(lambda x,y:x+'.'+y,subscriber_name,subscriber_id))

print(target_systum)