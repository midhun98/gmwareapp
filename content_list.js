function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function deleteItem(item) {
    $.ajax({
        method: 'DELETE',
        url: 'api/content/' + item + '/',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        success: function () {
            swal.fire('Deleted!');
            $("#list-cards" + item).hide();
        }
    });
}

function editBrand(item) {
    $.ajax({
        url: 'api/content/' + item + '/',
        type: "GET",
        success: function (response) {
            $('#form_name').val(String(response.data.name));
            $('#form_subject').val(String(response.data.subject));
            // $('#form_image').attr('href', String(response.data.image));
            $('#channel_pk').val(String(response.data.channel.id));
            $('#marketplace_pk').val(String(response.data.marketplace.id));
            $('#brand_pk').val(String(response.data.brands.id));
        }
    });

    $('#post-form').submit(function (e) {
        var formData = new FormData(e.target);
        e.preventDefault();
        $.ajax({
            url: 'api/content/' + item + '/',
            type: "PATCH",
            data: formData,
            processData: false,
            contentType: false,
            headers: {'X-CSRFToken': csrftoken},
            mimeType: "multipart/form-data",
            success: function () {
                swal.fire("Updated!");
                setTimeout(function () {
                    window.location.href = "content-list";
                }, 2000);

            }
        });
    });
}

function editImage(item) {
    $('#post-image').submit(function (e) {
        var formData = new FormData(e.target);
        e.preventDefault();
        $.ajax({
            url: 'api/content/' + item + '/',
            type: "PATCH",
            data: formData,
            processData: false,
            contentType: false,
            headers: {'X-CSRFToken': csrftoken},
            mimeType: "multipart/form-data",
            success: function () {
                swal.fire("Updated!");
                setTimeout(function () {
                    window.location.href = "content-list";
                }, 2000);
            }
        });
    });
}


var myArray = [];

$.ajax({
    method: 'GET',
    url: 'api/content/',
    success: function (response) {
        myArray = response;
        buildTable(myArray);
    }
});

function buildTable(data) {
    var table = document.getElementById('list-cards');
    for (i in data) {
        channel_dict = JSON.stringify(data[i]['channel']);
        marketplace_dict = JSON.stringify(data[i]['marketplace']);
        brands_dict = JSON.stringify(data[i]['brands']);
        try {
            channel_dict_name = JSON.parse(channel_dict).name;
        } catch (err) {
            channel_dict_name = "No channel";
        }
        try {
            marketplace_dict_img = JSON.parse(marketplace_dict).logo;
            marketplace_dict_name = JSON.parse(marketplace_dict).name;
        } catch (err) {
            marketplace_dict_img = "No market Image";
            marketplace_dict_name = "No market name";
        }
        try {
            brands_dict_img = JSON.parse(brands_dict).image;
        } catch (err) {
            brands_dict_img = "No market Image";
        }
        var row = `<div id=list-cards${data[i].id}>
                           <div class="card">
                               <div class="card-body" id=list-cards-${data[i].id}>
                                   <img class="card-img-bottom two" src="${data[i].image}" alt="No image" style="width: 30rem;" >
                                   <img class="card-img-bottom two" src="${marketplace_dict_img}" alt="No market Image" style="width: 10rem;" >
                                   <img class="card-img-bottom two" src="${brands_dict_img}" alt="No Brand Image" style="width: 10rem;" >
                                   <h5 class="card-title" style="color: black">${data[i].name}</h5>
                                   <p class="card-text"><span><b>Content</b></span></p>
                                   <p class="card-text">${data[i].subject}</p>
                                   <p class="card-text"><span><b>Channel Name: </b></span> ${channel_dict_name}</p>
                                   <p class="card-text"><span><b>Market Name: </b></span> ${marketplace_dict_name}</p>
                               </div>
                               <div>
                                   <button class="btn btn-danger" onclick="deleteItem(${data[i].id})">Delete</button>
                                   </button>
                                    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal"
                                        onclick="editBrand(${data[i].id})">Edit</button>
                                    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModalImage"
                                        onclick="editImage(${data[i].id})">Edit Image</button>
                               </div>
                           </div>
                       </div>
`

        table.innerHTML += row;
    }
}

