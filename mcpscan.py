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

import re
import urllib2

mcp_re = re.compile('.+/mcp(\d+.*)\.(zip|7z)$')
mf_re = re.compile('.+mediafire\.com/.+$')

def match_url(url):
	global mcp_re
	global mf_re
	r = mcp_re.match(url)
	if r: return (url, r.groups()[0])
	elif mf_re.match(url):
		r = urllib2.urlopen(url)
		mf_url = r.geturl()
		r = mcp_re.match(mf_url)
		if r: return (mf_url, r.groups()[0])

def insert_url(tweets, tweet, mf_url):
	(url, version) = mf_url
	obj = {'url': url, 'id': str(tweet.id), 'timestamp': tweet.created_at}
	for i in range(len(tweets)):
		if long(tweets[i]['id']) < tweet.id:
			tweets.insert(i, obj)
			print "MCP %s: %s" % (version, url)
			return
	print "MCP %s: %s" % (version, url)
	tweets.append(obj)

def update_tweets(urls, tweets, timeline):
	updated = False
	for tweet in timeline:
		for url in [u.expanded_url for u in tweet.urls]:
			mf_url = match_url(url)
			if mf_url and not mf_url[0] in urls:
				insert_url(tweets, tweet, mf_url)
				urls.add(mf_url[0])
				updated = True
	return updated

