document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('#form').onsubmit = () => {
    const curr = document.querySelector('#currency').value;

    //creo una nueva request que ejecuta metodo POST y busca la ruta /convert en currendy.py
    const request = new XMLHttpRequest();
    request.open("POST","/convert");

    //crea un formulario pero con la variable curr que habíamos colocado dentro del campo currency
    const data = new FormData();
    data.append('currency',curr);

    //envía el request
    request.send(data);

    //despues de ser enviado el request se ejecuta esta parte
    request.onload = () => {
      const data = JSON.parse(request.responseText);

      if (data.success) {
        const content = "1 USD is equal to " + data.rate + " " + curr
        document.querySelector('#result').innerHTML = content
      } else {
        document.querySelector('#result').innerHTML = "There was an error.";
      };
    };

    //no realizar el submit del form
    return false;
  };
});
