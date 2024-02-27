const { expect } = require('chai');
const calculateNumbers = require('./1-calcul');

describe('calculateNumbers', function() {
  describe('SUM operation', function() {
    it('should return the sum of two rounded numbers', function() {
      expect(calculateNumbers('SUM', 3.6, 7.2)).to.equal(11);
    });
  });

  describe('SUBTRACT operation', function() {
    it('should return the difference between two rounded numbers', function() {
      expect(calculateNumbers('SUBTRACT', 10.5, 4.8)).to.equal(6);
    });
  });

  describe('DIVIDE operation', function() {
    it('should return the result of dividing two rounded numbers', function() {
      expect(calculateNumbers('DIVIDE', 15, 3)).to.equal(5);
    });

    it('should return "Error" when trying to divide by zero', function() {
      expect(calculateNumbers('DIVIDE', 10, 0)).to.equal('Error');
    });
  });

  describe('Invalid operation type', function() {
    it('should throw an error for an invalid operation type', function() {
      expect(() => {
        calculateNumbers('INVALID_OPERATION', 5, 2);
      }).to.throw(Error);
    });
  });
});
