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

  //dialog.flows(intents);
/*  dialog.flow('kaboe003:PatientIntent', (msg, flow) => {
    console.log('PatientIntent');
    createObject();
    piz = msg.slots[0].value.value;
    params.Item.id = piz;

    flow.continue('kaboe003:ZSTIntent', (msg, flow) => {
      console.log('ZSTIntent');
      zst = msg.slots[0].value.value
      params.Item.info.push({'Zahnstein': zst});
      flow.continue('kaboe003:MUIntent', (msg, flow) => {
        console.log('MUIntent');
        mu = msg.slots[0].value.value
        params.Item.info.push({'Mundkrankheit': mu});
        flow.continue('kaboe003:ZahnIntent', (msg, flow) => {
          var quadrant = msg.slots[0].value.value;
          var zahn = msg.slots[1].value.value;
          var zstatus = msg.slots[2].value.value;
          var zaehne = quadrant.toString() + zahn.toString();
          console.log(zaehne);
          params.Item.zaehne.push({[zaehne]:zstatus});
          console.log('ZahnIntent' + ' ' );
          cont();
        })
      })

    })
    function cont(){
      flow.continue('kaboe003:ZahnIntent', (msg, flow) => {
        if (msg.slots[0].value.value == 'Stop'){
        console.log('Stop');
        //testmap.set("info", info);
        //testmap.set("zaehne", zaehne);
        docClient.put(params, function(err, data) {
          if (err) console.log(err);
          else console.log(data);
        });

        console.log(params);

        flow.end();
      } else {
      console.log('ZahnIntent fortgesetzt' + ' ' );
      var quadrant = msg.slots[0].value.value;
      var zahn = msg.slots[1].value.value;
      var zstatus = msg.slots[2].value.value;
      var zaehne = quadrant.toString() + zahn.toString();
      params.Item.zaehne.push({[zaehne]:zstatus});

      cont();
    }

      })
    }

  })*/

dialog.flow('kaboe003:PatientIntent', (msg, flow) => {
  console.log("Test");
})

});
function setZahn(quadrant, zahn, wert){
  zaehne.set(`${quadrant}${zahn}`, wert);
  console.log(zaehne);
}

function createItem(piz, zstWert, muWert, quadrant, zahn, zahnWert){
  //Item.
}

function createObject(){
  params.TableName = "TeethCounter";
  params.Item ={};
  params.Item.zaehne = [];
  params.Item.info = [];
  console.log(params);
}






//});
