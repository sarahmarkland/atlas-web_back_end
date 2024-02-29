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

describe('Login endpoint', function() {
  it('Correct status code for POST /login', function(done) {
    request.post({ url: 'http://localhost:7865/login', json: { userName: 'JohnDoe' } }, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct welcome message for POST /login', function(done) {
    request.post({ url: 'http://localhost:7865/login', json: { userName: 'JohnDoe' } }, function (error, response, body) {
      expect(body).to.equal('Welcome JohnDoe');
      done();
    });
  });

  it('Error message for missing username in POST /login', function(done) {
    request.post({ url: 'http://localhost:7865/login', json: {} }, function (error, response, body) {
      expect(response.statusCode).to.equal(400);
      expect(body).to.equal('Username is required');
      done();
    });
  });
});

describe('Available payments endpoint', function() {
  it('Correct status code for GET /available_payments', function(done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct payment methods for GET /available_payments', function(done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      const responseBody = JSON.parse(body);
      expect(responseBody).to.deep.equal({ payment_methods: { credit_cards: true, paypal: false } });
      done();
    });
  });
});
