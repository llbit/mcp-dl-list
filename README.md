mcp-dl-list
===========

Scrapes MCP download links from a twitter timeline.

View the live page at [http://mcp.llbit.se](http://mcp.llbit.se).

The `pulltweets.py` Python script downloads the latest 100 tweets from twitter
and scans them for MCP download links. The `scanall.py` script requests all
tweets in batches of 100, with 15 sec delay between requests.

To run the scripts you must create a `config.json` file containing these lines:

    {
      "consumer_key": "...",
      "consumer_secret": "...",
      "access_token_key": "...",
      "access_token_secret": "...",
    }

The ellipsis indicate where you should enter your API keys.  See the
python-twitter docs for more info.

