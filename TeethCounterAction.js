const { withHermes } = require('hermes-javascript')

withHermes(hermes => {
  const dialog = hermes.dialog()

  dialog.flow('ZahnsteinIntent', (msg, flow) => {
    console.log(msg))
    flow.end()
    return "Testlog"
  })
})
