import sched, time, requests

s = sched.scheduler(time.time, time.sleep)
def check_all(sc): 
	for n in ["https://RAIDNODE.ignaciopardo.repl.co"]:
		while 'class="RAID_NODE"' not in (stat := requests.get(n).text):
			print(stat)
			continue
	print(stat)
	s.enter(1, 1, check_all, (sc,))

s.enter(1, 1, check_all, (s,))
s.run()