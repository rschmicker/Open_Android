var defaultOptions = {
  listenPort: 8080,
  validHttpMethods: ['GET'],
  validPaths: ['/solr/apps/select'],
  invalidParams: ['qt', 'stream'],
  backend: {
    host: 'localhost',
    port: 8983
  }
};

var SolrProxy = require('solr-proxy');
SolrProxy.start();
