// Variables to store the user preference inputs
// Type: string
var temp_range;
// Type: string
var population;
// Type: Integer
var square_feet;
// Type: Integer
var price;
// Type: Integer
var beds;
// Type: Integer
var baths;
// Type: Integer
var lotSize;
// Type: Integer
var hoa_permonth;

// --------------------------------------------------
//  TEMPERATURE INPUT
// Select the temperature input dropdown menu
var tempMenu = d3.select("#temp-input");
temp_range = tempMenu.property("value");

// Function to handle changes in the temperature selection dropdown menu
function selectTemp() {
    temp_range = tempMenu.property("value");
    console.log(`Temperature Range Selected: ${temp_range}`) 
}

// --------------------------------------------------
// POPULATION INPUT
// Select the population size input dropdown menu
var populationMenu = d3.select("#popSize-input");
population = (populationMenu.property("value"));

// Function to handle changes in the population size selection dropdown menu
function selectPopSize() {
    population = populationMenu.property("value");
    console.log(`Population Selected: ${population}`) 
}

// --------------------------------------------------
//  SQUARE-FOOTAGE INPUT
// Select the square-footage input dropdown menu
var squareFeetMenu = d3.select("#squareFeet-input");
square_feet = parseInt(squareFeetMenu.property("value"));

// Function to handle changes in the square-footage selection dropdown menu
function selectSquareFeet() {
    square_feet = parseInt(squareFeetMenu.property("value"));
    console.log(`Square-footage Selected: ${square_feet}`) 
    return square_feet;
}

// --------------------------------------------------
// PRICE INPUT
// Select the budget input dropdown menu
var budgetMenu = d3.select("#budget-input");
price = parseInt(budgetMenu.property("value"));

// Function to handle changes in the budget selection dropdown menu
function selectBudget() {
    price = parseInt(budgetMenu.property("value"));
    console.log(`Price Selected: ${price}`) 
    return price;
}

// --------------------------------------------------
// BEDROOM INPUT
// Select the bedroom input dropdown menu
var bedroomMenu = d3.select("#bedroom-input");
beds = parseInt(bedroomMenu.property("value"));

// Function to handle changes in the bedroom selection dropdown menu
function selectBedrooms() {
    beds = parseInt(bedroomMenu.property("value"));
    console.log(`Number of Bedrooms Selected: ${beds}`) 
    return beds;
}

// --------------------------------------------------
// BATHROOM INPUT
// Select the bathroom input dropdown menu
var bathroomMenu = d3.select("#bathroom-input");
baths = parseInt(bathroomMenu.property("value"));

// Function to handle changes in the bathroom selection dropdown menu
function selectBathrooms() {
    baths = parseInt(bathroomMenu.property("value"));
    console.log(`Number of Bathrooms Selected: ${baths}`) 
    return baths;
}

// --------------------------------------------------
// LOT SIZE INPUT
// Select the lot size input dropdown menu
var lotSizeMenu = d3.select("#lotSize-input");
lotSize = lotSizeMenu.property("value");

// Function to handle changes in the lot size selection dropdown menu
function selectLotSize() {
    lotSize = lotSizeMenu.property("value");
    console.log(`Lot Size Selected: ${lotSize}`) 
    return lotSize;
}

// --------------------------------------------------
// HOA FEE INPUT
// Select the HOA fee input dropdown menu
var hoaMenu = d3.select("#hoa-input");
hoa_permonth = parseInt(hoaMenu.property("value"));

// Function to handle changes in the HOA fee selection dropdown menu
function selectHoaBudget() {
    hoa_permonth = parseInt(hoaMenu.property("value"));
    console.log(`HOA budget Selected: ${hoa_permonth}`) 
    return hoa_permonth;
}

// --------------------------------------------------
// SUBMIT BUTTON   
// Array to store the user inputs
var userInputs;

// function to handle clicks on the submit button
function submitInput() {
    // Clear the user input array
    userInputs = [];
    // Push the user inputs to the userInputs array
    userInputs.push(temp_range);
    userInputs.push(population);
    userInputs.push(square_feet);
    userInputs.push(price);
    userInputs.push(beds);
    userInputs.push(baths);
    userInputs.push(lotSize);
    userInputs.push(hoa_permonth);
    console.log(`Input submitted: ${userInputs}`);
    console.log(userInputs);
    return userInputs;
}

// $(document).ready(function() {
//     $("#button").bind('click', function(){
//         //Get all words from list
//         var list = [];
//         $("#wordlist option").each(function(){
//             list.push($(this).val());
//         });
//         //var list = $( "#wordlist option" ).val();
//         console.log(list);
//         $.getJSON($SCRIPT_ROOT + '/_array2python', {
//             wordlist: list.toString()
//         }, function(data){
//             console.log(data.result)
//             $( "#result" ).text(data.result);
//         });
//         return false;
//     });
// });