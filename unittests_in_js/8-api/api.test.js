const chai = require('chai');
const chaiHttp = require('chai-http');
const { expect } = chai;
const server = require('./api');

chai.use(chaiHttp);

describe('Index Page', function() {
  it('should return status code 200', function(done) {
    chai.request(server)
      .get('/')
      .end(function(err, res) {
        expect(res).to.have.status(200);
        done();
      });
  });

  it('should return "Welcome to the payment system"', function(done) {
    chai.request(server)
      .get('/')
      .end(function(err, res) {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});