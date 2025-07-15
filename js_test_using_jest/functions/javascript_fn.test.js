// javascript_fn.test.js

const {
  calculateDiscount,
  filterProducts,
  sortProducts,
  validateEmail
} = require('./javascript_fn');

// -------------------------
// calculateDiscount Tests
// -------------------------
describe('calculateDiscount', () => {
  test('returns correct discount value', () => {
    expect(calculateDiscount(100, 10)).toBe(90);
    expect(calculateDiscount(200, 25)).toBe(150);
  });

  test('returns same value if discount is 0', () => {
    expect(calculateDiscount(150, 0)).toBe(150);
  });

  test('returns 0 if discount is 100', () => {
    expect(calculateDiscount(500, 100)).toBe(0);
  });

  test('throws error for negative price', () => {
    expect(() => calculateDiscount(-100, 10)).toThrow('Invalid input');
  });

  test('throws error for invalid discount values', () => {
    expect(() => calculateDiscount(100, -5)).toThrow('Invalid input');
    expect(() => calculateDiscount(100, 110)).toThrow('Invalid input');
  });
});

// -------------------------
// filterProducts Tests
// -------------------------
describe('filterProducts', () => {
  const sampleProducts = [
    { name: 'Laptop' },
    { name: 'Phone' },
    { name: 'Tablet' },
    { name: 'Smartwatch' }
  ];

  test('filters products by query (case-insensitive)', () => {
    const result = filterProducts(sampleProducts, 'phone');
    expect(result).toEqual([{ name: 'Phone' }]);
  });

  test('returns multiple matches', () => {
    const result = filterProducts(sampleProducts, 't');
    expect(result).toEqual([
      { name: 'Laptop' },
      { name: 'Tablet' },
      { name: 'Smartwatch' }
    ]);
  });

  test('returns empty array if no matches', () => {
    const result = filterProducts(sampleProducts, 'camera');
    expect(result).toEqual([]);
  });

  test('throws error for non-array products', () => {
    expect(() => filterProducts('not-an-array', 'query')).toThrow('Invalid input');
  });

  test('throws error for non-string query', () => {
    expect(() => filterProducts(sampleProducts, 123)).toThrow('Invalid input');
  });
});

// -------------------------
// sortProducts Tests
// -------------------------
describe('sortProducts', () => {
  const sampleProducts = [
    { name: 'Tablet', price: 200 },
    { name: 'Phone', price: 100 },
    { name: 'Laptop', price: 300 }
  ];

  test('sorts by price (ascending)', () => {
    const result = sortProducts([...sampleProducts], 'price');
    expect(result).toEqual([
      { name: 'Phone', price: 100 },
      { name: 'Tablet', price: 200 },
      { name: 'Laptop', price: 300 }
    ]);
  });

  test('sorts by name (alphabetical)', () => {
    const result = sortProducts([...sampleProducts], 'name');
    expect(result).toEqual([
      { name: 'Laptop', price: 300 },
      { name: 'Phone', price: 100 },
      { name: 'Tablet', price: 200 }
    ]);
  });

  test('throws error for invalid key', () => {
    expect(() => sortProducts(sampleProducts, 'weight')).toThrow('Invalid input');
  });

  test('throws error if products is not an array', () => {
    expect(() => sortProducts('not-an-array', 'price')).toThrow('Invalid input');
  });
});

// -------------------------
// validateEmail Tests
// -------------------------
describe('validateEmail', () => {
  test('returns true for valid emails', () => {
    expect(validateEmail('test@example.com')).toBe(true);
    expect(validateEmail('user.name+tag@domain.co')).toBe(true);
    expect(validateEmail('a@b.c')).toBe(true);
  });

  test('returns false for invalid emails', () => {
    expect(validateEmail('plainaddress')).toBe(false);
    expect(validateEmail('@missingusername.com')).toBe(false);
    expect(validateEmail('username@.com')).toBe(false);
    expect(validateEmail('username@domain')).toBe(false);
    expect(validateEmail('username@domain..com')).toBe(false);
  });

  test('throws error for non-string input', () => {
    expect(() => validateEmail(null)).toThrow('Invalid input');
    expect(() => validateEmail(undefined)).toThrow('Invalid input');
    expect(() => validateEmail(123)).toThrow('Invalid input');
    expect(() => validateEmail({})).toThrow('Invalid input');
  });
});
