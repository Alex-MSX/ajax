document.addEventListener('DOMContentLoaded', () => {

  //conectar al web socket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  //cuando doy click al boton, este emite el resultado al servidor votes.py quien ejecuta la función 'submit vote'
  socket.on('connect', () => {
    document.querySelectorAll("button").forEach(button => {
        button.onclick = () => {
          const selection = button.dataset.vote;
          socket.emit('submit vote',{'selection':selection})
        };
    });
  });

  //al ejecutar la funcion 'announce vote' agrega un li a mi html
  socket.on('announce vote', data => {
    const li = document.createElement('li');
    li.innerHTML = "Vote recorded: " + data.selection;
    document.querySelector('#votes').append(li);
  });

});
