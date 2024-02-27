const assert = require('assert');
const calculateNumbers = require('./1-calcul');

describe('calculateNumbers', function() {
  describe('SUM operation', function() {
    it('should return the sum of two rounded numbers', function() {
      assert.strictEqual(calculateNumbers('SUM', 3.6, 7.2), 11);
    });
  });

  describe('SUBTRACT operation', function() {
    it('should return the difference between two rounded numbers', function() {
      assert.strictEqual(calculateNumbers('SUBTRACT', 10.5, 4.8), 6);
    });
  });

  describe('DIVIDE operation', function() {
    it('should return the result of dividing two rounded numbers', function() {
      assert.strictEqual(calculateNumbers('DIVIDE', 15, 3), 5);
    });

    it('should return "Error" when trying to divide by zero', function() {
      assert.strictEqual(calculateNumbers('DIVIDE', 10, 0), 'Error');
    });
  });

  describe('Invalid operation type', function() {
    it('should throw an error for an invalid operation type', function() {
      assert.throws(() => {
        calculateNumbers('INVALID_OPERATION', 5, 2);
      }, Error);
    });
  });
});
