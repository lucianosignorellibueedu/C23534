function getPosts() {
    return new Promise((resolve, reject) => {
      fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => {
          if (!response.ok) {
            throw new Error('Error en la solicitud');
          }
          return response.json();
        })
        .then(posts => {
          resolve(posts);
        })
        .catch(error => {
          reject(error);
        });
    });
  }
  
  // Llama a la función getPosts para obtener los datos de la API
  getPosts()
    .then(posts => {
      console.log('Publicaciones obtenidas con éxito:');
      console.log(posts);
    })
    .catch(error => {
      console.error('Hubo un error al obtener las publicaciones:', error);
    });
  