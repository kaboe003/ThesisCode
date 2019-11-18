const { withHermes } = require('hermes-javascript')
const aws = require("aws-sdk");
var dynamoDB = new aws.DynamoDB();
var docClient = new AWS.DynamoDB.DocumentClient();
var zst;
var mu;
var zaehne = new Map();
var info = new Map();
var piz;
var params = {
  TableName:TeethCounter,
  Item:{
    "piz" = piz.toString(),
    "zaehne" = zaehne,
    "info" = info
  }
}

aws.config.update({
  region: "eu-central-1"
  endpoint: "http://localhost:60"
});

withHermes(hermes => {
  const dialog = hermes.dialog()
  dialog.flow('kaboe003:PatientIntent', (msg, flow) => {
    piz = msg.slots[0].value.value;
    console.log(msg))
    flow.end()
    return "Guten Tag Patient" + msg.slots[0].value.value
  })
  dialog.flow('kaboe003:ZSTIntent', (msg, flow) => {
    zst = msg.slot[0].value.value;
    info.set('Zahnstein', zst);
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('kaboe003:MUIntent', (msg, flow) => {
    mu = msg.slot[0].value.value;
    info.set("Mundkrankheit", mu);
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('kaboe003:ZahnIntent', (msg, flow) => {
    if (zaehne.size() <= 32){
    zaehne.set('${msg.slots[0].value.value}${msg.slots[1].value.value, msg.slots[2].value.value}')
    console.log(msg))
    flow.end()
    return "Verstanden"
  }
  flow.end()
  return "Es sind bereits alle 32 Zähne erfasst."
  })
  dialog.flow('kaboe003:StopIntent', (msg, flow) => {
    console.log(msg))
    docClient.put(params)
    flow.end()
    return "Patient" + piz +"gespeichert"
  })

});
