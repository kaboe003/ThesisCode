const { withHermes } = require('hermes-javascript')
var zst;
var mu;
var zaehne = new Map();
var info = new Map();
var piz;
withHermes(hermes => {
  const dialog = hermes.dialog()
  dialog.flow('PatientIntent', (msg, flow) => {
    piz = msg.slots[0].value.value;
    console.log(msg))
    flow.end()
    return "Guten Tag Patient" + msg.slots[0].value.value
  })
  dialog.flow('ZSTIntent', (msg, flow) => {
    zst = msg.slot[0].value.value;
    info.set('Zahnstein', zst);
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('MUIntent', (msg, flow) => {
    mu = msg.slot[0].value.value;
    info.set("Mundkrankheit", mu);
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('ZahnIntent', (msg, flow) => {
    if (zaehne.size() <= 32){
    zaehne.set('${msg.slots[0].value.value}${msg.slots[1].value.value, msg.slots[2].value.value}')
    console.log(msg))
    flow.end()
    return "Verstanden"
  }
  flow.end()
  return "Es sind bereits alle 32 Zähne erfasst."
  })

})
