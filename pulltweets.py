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
import sys

from sets import Set
from datetime import datetime
from mcpscan import update_tweets

with open('config.json') as f:
	config = json.load(f)
try:
	with open('data.json') as f:
		data = json.load(f)
except:
	data = {'urls': [], 'timestamp': datetime.now().isoformat()}

# tweet list assumed to be in reverse chronological order!
tweets = data['urls']
urls = Set([t['url'] for t in tweets])

# access latest tweets
api = twitter.Api(**config)
timeline = api.GetUserTimeline(screen_name='SeargeDP', count=100)

if update_tweets(urls, tweets, timeline):
	data['timestamp'] = datetime.now().isoformat()
	with open('data.json', 'w') as f:
		json.dump(data, f)
else:
	sys.exit(1)
