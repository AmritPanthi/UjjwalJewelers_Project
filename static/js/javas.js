var x = document.getElementById("login");
var y = document.getElementById("signup");
var z = document.getElementById("btn");

function signup (){
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "198px";
}

function login(){
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0";
}

const searchBox = document.querySelector('.search-box');
const searchBtn = document.querySelector('#search-btn');
searchBtn.addEventListener('click', (event) => {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'show' );
  xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
  xhr.onload = () => {
      const data = JSON.parse(xhr.responseText);
      //console.log(xhr.responseText);
      
      const table = document.querySelector('.table-dark');
      let html =`
                  <tr>
                     <th>name</th>
                      <th>price</th>
                      <th>details</th>
                      <th>actions</th>
                      </tr>
            `;
      for(d in data){
          
          html += '<tbody>';
          html += '<tr>';
          html += `<td>${data[d].name}</td>`;
          html += `<td>${data[d].price}</td>`;
          html += `<td>${data[d].details}</td>`;
          html += `<td>
          <a href="update/${data[d].id}"><span class="btn btn-success">Update</span></a>
          <a href="delete/${data[d].id}"><span class="btn btn-danger">Delete</span></a>
          </td>`;
          html += '</tr>';
          html += '</tbody>';
      }
      
      table.innerHTML = html;

  }
  const data = new FormData();
  data.append('searchTerm', searchBox.value);
  xhr.send(data);
  return false;
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
