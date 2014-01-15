# coding=utf-8
# Copyright (c) 2014, Jesper Öqvist <jesper@llbit.se>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import twitter
import re
from sets import Set
from datetime import datetime
mcp_re = re.compile('.+/mcp(\d+).zip$')
with open('config.json') as f:
	config = json.load(f)
try:
	with open('data.json') as f:
		data = json.load(f)
except:
	data = {'urls': [], 'timestamp': datetime.now().isoformat()}

urls = Set()
for link in data['urls']:
	urls.add(link['url'])

updated = False

# access latest tweets
api = twitter.Api(**config)
for tweet in api.GetUserTimeline(screen_name='SeargeDP'):
	for url in [u.expanded_url for u in tweet.urls]:
		r = mcp_re.match(url)
		if r and not url in urls:
			data['urls'].append({'url': url, 'tweet': tweet.id})
			print "MCP %s: %s" % (r.groups()[0], url)
			updated = True

if updated:
	data['timestamp'] = datetime.now().isoformat()
	with open('data.json', 'w') as f:
		json.dump(data, f)
