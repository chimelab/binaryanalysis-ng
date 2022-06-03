# Configuration of the OpenSearch reporter in BANG

BANG can write its results to OpenSearch and make it available
for further investigation and processing using standard
OpenSearch tools.

Note: these are mostly personal notes for installation and configuration of
Amazon's OpenSearch on Fedora. The version described is 2.0.0.

In this fork a few components were renamed:

* ElasticSearch -> OpenSearch
* Kibana -> OpenSearch Dashboards

It could be that ElasticSearch will work as well, but this hasn't been tested.

## Installing OpenSearch

(Installing OpenSearch and OpenSource Dashboards is outside the scope of this
document and is described on the OpenSearch website, just a few notes are put
here.)

Install `opensearch`

## Configuring OpenSearch

For now it should be run without SSL, so you need to change settings in:

    /etc/opensearch/opensearch.yml

and replace:

    plugins.security.ssl.http.enabled:: true

with:

    plugins.security.ssl.http.enabled: false

and restart OpenSearch:

    # systemctl start opensearch.service

Please note that this *will* be changed in the future.

## Install OpenSearch Dashboards

Install `opensearch-dashboards`

Then edit:

    /etc/opensearch-dashboards/opensearch_dashboards.yml

and change:

    opensearch.hosts: [https://localhost:9200]

into:

    opensearch.hosts: [http://localhost:9200]

(note the change from `https` to `http`!)

and start OpenSearch Dashboards:

    # systemctl start opensearch-dashboards.service

### Creating a user

Users can be added in OpenSearch Dashboards. Please note: user names are case
sensitive!

Also, OpenSearch doesn't like passwords shorter than 5 characters. In the rest
of the document it is assumed that the user is `bang` and the password is
`bangbang`.

The index that will be used for OpenSearch is `bang`.

## Installing OpenSearch Python bindings

Install:

    python3-elasticsearch

# Configure BANG to use OpenSearch

The file bang.config has a section 'opensearch'. In these the following
should be changed:

    opensearch_enabled = no

should be changed to:

    opensearch_enabled = yes

# References

[1] <https://opensearch.org/>
