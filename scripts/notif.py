import os
def notify(title, link, message):
	t = '-title {!r}'.format(title)
	m = '-message {!r}'.format(message)
	o = '-open {!r}'.format(link)
	s = '-sound Crystal'
	i = '-appIcon icon.icns'
	e = '-sender com.apple.timemachine'
	os.system('terminal-notifier {}'.format(' '.join([t, m, o, s, i, e])))


notify(title = 'Auto Zoom', link = 'http://google.com', message  = 'Background')