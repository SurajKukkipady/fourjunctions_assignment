// javascript_fn.js

function calculateDiscount(price, discount) {
  if (price < 0 || discount < 0 || discount > 100) {
    throw new Error('Invalid input');
  }
  return price - (price * discount / 100);
}

function filterProducts(products, query) {
  if (!Array.isArray(products) || typeof query !== 'string') {
    throw new Error('Invalid input');
  }
  return products.filter(product =>
    product.name.toLowerCase().includes(query.toLowerCase())
  );
}

function sortProducts(products, key) {
  if (!Array.isArray(products) || (key !== 'name' && key !== 'price')) {
    throw new Error('Invalid input');
  }
  return products.sort((a, b) => {
    if (key === 'price') {
      return a.price - b.price;
    } else {
      return a.name.localeCompare(b.name);
    }
  });
}

function validateEmail(email) {
  if (typeof email !== 'string') {
    throw new Error('Invalid input');
  }
  // Improved regex to disallow ".." in domain
  const emailRegex = /^[^\s@]+@[^\s@.]+(?:\.[^\s@.]+)+$/;
  return emailRegex.test(email);
}

module.exports = {
  calculateDiscount,
  filterProducts,
  sortProducts,
  validateEmail
};
