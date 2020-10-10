from py_adventure import *

travel1 : Event = Event('bg_e_01', 'travel', 'Player travelled from Baldur\'s Gate to Elturel.')
interact1 : Event = Event('barrel_01', 'interact', 'Player searched a barrel.')
result1 : Event = Event('barrel_02', 'result', 'Player found a sword.')
travel2 : Event = Event('e_bg_01', 'travel', 'Player travelled from Elturel to Baldur\'s Gate.')

event_log : EventLog = EventLog()

event_log.log(travel1)
event_log.log(interact1)
event_log.log(result1)
event_log.log(travel2)

print(event_log)
print('')
print(event_log.get_last())
print(event_log.get('barrel_01'))
print(event_log.get_last_of_type('result'))
