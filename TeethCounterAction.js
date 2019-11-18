const { withHermes } = require('hermes-javascript')

withHermes(hermes => {
  const dialog = hermes.dialog()

  dialog.flow('ZSTIntent', (msg, flow) => {
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('MUIntent', (msg, flow) => {
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('ZahnIntent', (msg, flow) => {
    console.log(msg))
    flow.end()
    return "Verstanden"
  })
  dialog.flow('PatientIntent', (msg, flow) => {
    console.log(msg))
    flow.end()
    return "Guten Tag Patient" + msg.slots[0].value.value
  })
})
