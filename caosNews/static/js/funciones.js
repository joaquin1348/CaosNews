let url = "https://apis.digital.gob.cl/fl/feriados"
    
    
$.get(url, function(respuesta) {
   
    respuesta.forEach(function(item){
        if (item.fecha.includes("2021")) {
            var li = document.createElement('li')
            li.innerHTML += `${item.fecha} // ${item.nombre}`; 
            document.getElementById("lista-feriados").appendChild(li);

     
        }

        })
    

}, "json");



// function fetchTodo() {
//     fetch("https://apis.digital.gob.cl/fl/feriados")
//     .then(function(data){

//         return data.json();
//     })
//     .then(function(data){

//         var datos = document.getElementById("lista-feriados");

//         datos.innerHTML = `<li> ${data[0].fecha} </li>`;
        
//     })
// };