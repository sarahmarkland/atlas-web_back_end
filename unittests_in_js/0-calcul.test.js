const assert = require('assert');
const calculateNumbers = require('./0-calcul');

describe('calculateNumbers', function() {
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(3.6, 7.2), 11);
  });
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(-3.3, -7.7), -11);
  });
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(3.6, -7.2), -3);
  });
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(-3.6, 7.2), 3);
  });
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(3.4, 0), 3);
  });
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(0, 7.6), 8);
  });
  it('should return the sum of two rounded numbers', function() {
    assert.strictEqual(calculateNumbers(0, 0), 0);
  });
});
