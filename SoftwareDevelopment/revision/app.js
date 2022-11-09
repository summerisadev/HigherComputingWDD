// Book Ordering, but in JS

// Helper Packages
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

// Init constants
const bookName = "JavaScript for Dummies"
const bookCost = 15.99
const currentVoucherCode = "Z2VuZXJhdG9y"
let activeDiscount = 0
let isvoucherActive = false
let quantity = 0

console.clear()

/**
 * Gets user input to provide a quantity
 * @returns { Number } quantity - Quantity of requested books
 */
async function getQuantity()
{
    readline.question('How many books are you ordering?', qnty => {
        readline.close();
        return qnty;
    });
}

console.log(`${bookName} CLI Ordering Utility`)
quantity = getQuantity()


while (quantity > 80 || quantity < 1)
{
    console.clear()
    console.log('Quantity cannot be more than 80 or less than 1.')
    quantity = getQuantity()
}


