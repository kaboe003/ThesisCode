const { withHermes } = require('hermes-javascript');
const aws = require("aws-sdk");

var dynamoDB = new aws.DynamoDB();
var docClient = new aws.DynamoDB.DocumentClient();
var zst;
var mu;
var zstatus;
var piz;
var params= {}


aws.config.update({
  region: 'eu-central-1',
  endpoint: 'http://localhost:8000'
});



withHermes((hermes, done) => {
  const dialog = hermes.dialog()

dialog.flow("kaboe003:PatientIntent", (msg, flow) => {
  console.log("Test"); 
})






//});
