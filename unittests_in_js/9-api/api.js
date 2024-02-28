// api.js
const express = require('express');

const app = express();
const PORT = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const cartId = req.params.id;
  if (!/^\d+$/.test(cartId)) {
    return res.status(400).send('Invalid cart ID. Must be a number');
  }
  res.send(`Payment methods for cart ${cartId}`);
});

const server = app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = server;
