// api.test.js
const request = require('request');
const expect = require('chai').expect;

describe('Cart page', function() {
  it('Correct status code when :id is a number', function(done) {
    request('http://localhost:7865/cart/123', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result when :id is a number', function(done) {
    request('http://localhost:7865/cart/123', function (error, response, body) {
      expect(body).to.equal('Payment methods for cart 123');
      done();
    });
  });

  it('Correct status code when :id is NOT a number', function(done) {
    request('http://localhost:7865/cart/abc', function (error, response, body) {
      expect(response.statusCode).to.equal(400);
      done();
    });
  });

  it('Correct error message when :id is NOT a number', function(done) {
    request('http://localhost:7865/cart/abc', function (error, response, body) {
      expect(body).to.equal('Invalid cart ID. Must be a number');
      done();
    });
  });
});