console.log('Request Data...')

//setTimeout(() => {
//  console.log('Preparing Data...')

//  const backendData = {
//    serever: 'scc',
//    port: 8080,
//    status: 'Working properly'
//  }
//
//  setTimeout(() => {
//    backendData.modified = true
//    console.log('Data recived', backendData)
//  }, 2000)
//}, 2000)

const prms = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('Preparing Data...')
    const backendData = {
      serever: 'scc',
      port: 8080,
      status: 'Working properly'
    }
    resolve(backendData)
  }, 2000)
})

//prms.then(data => {
//  console.log('Promise resolved', data)
//})
prms.then(data => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      data.modified = true
      resolve(data)
    }, 2000)
  })  
}).then(clientData => {
  console.log('Data resived', clientData)
})