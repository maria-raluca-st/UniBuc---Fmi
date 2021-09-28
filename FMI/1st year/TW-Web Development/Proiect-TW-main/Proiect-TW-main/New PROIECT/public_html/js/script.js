var modalSettings = document.getElementById("modalSettings");
var modalView = document.getElementById("modalView");
var modalAdd = document.getElementById("modalAdd");
var giftList = document.getElementById("gift-list");

const formTitle = document.getElementById("b-title");
const formDesc = document.getElementById("b-descript");




function checkGreeting() 
{
    if(!window.localStorage.getItem("username") || window.localStorage.getItem("username" == ""))
        document.getElementById("greeting").textContent = "Glad to see you!";
    else document.getElementById("greeting").textContent = "Glad to see you, " + window.localStorage.getItem("username") + "!";
}
window.onload = checkGreeting();

//functie pt activarea butonului de post
document.getElementById("b-title").addEventListener("keyup", function() 
{
    let Input = document.getElementById('b-title').value;
    if (Input != "") {
        document.getElementById('postBtn').removeAttribute("disabled");
    } else {
        document.getElementById('postBtn').setAttribute("disabled", null);
    }
});

//functie pt activarea butonului de post--varianta mobile
document.getElementById("modal-b-title").addEventListener("keyup", function() 
{
    let Input = document.getElementById('modal-b-title').value;
    if (Input != "") {
        document.getElementById('postMBtn').removeAttribute("disabled");
    } else {
        document.getElementById('postMBtn').setAttribute("disabled", null);
    }
});


function saveSettings() 
{
    var Nume = document.getElementById("user-name").value;
    window.localStorage.setItem("username", Nume);

    if(Nume != "")
      document.getElementById("greeting").textContent = "Glad to see you, " + Nume + "!";
    else 
      document.getElementById("greeting").textContent = "Glad to see you!";
    
    closeModal();
}
//functie pt butonul settings
function openSettings() {
    modalSettings.style.display = "block";
    document.body.style.position = "fixed";
}
//functie pt butonul de add pt ecrane mici
function openModalAdd() 
{
    modalAdd.style.display = "block";
    document.body.style.position = "fixed";
    document.getElementById("modal-b-title").value='';
    document.getElementById("modal-b-descript").value='';

}


function editViewModal(id, title, description) 
{
    let modal = document.getElementById("modalView-info");
    while(modal.firstChild) modal.removeChild(modal.firstChild);

    let modalTitle = document.createElement('h1');
    modalTitle.innerText = "Edit Item";
    modalTitle.classList.add("modal-title");

    let form = document.createElement('form');
    form.action = '/gifts/' + id;
    form.method = 'POST';
    form.id = "edit-form";

    let titleLabel = document.createElement('label');
    titleLabel.htmlFor = "gift-title";
    titleLabel.textContent = "Item Name";

    let titleInput = document.createElement('input');
    titleInput.name = "b-title";
    titleInput.id = "edit-b-title";
    titleInput.value = title;

    let descriptLabel = document.createElement('label');
    descriptLabel.htmlFor = "gift-description";
    descriptLabel.textContent = "Description";

    let descriptTextarea = document.createElement("textarea");
    descriptTextarea.name = "b-descript"
    descriptTextarea.id = "edit-b-descript";
    descriptTextarea.textContent = description;

    let menu = document.createElement('div');
    menu.classList.add("modal-menu");

    let saveBtn = document.createElement('button');
    saveBtn.type = "submit";
    saveBtn.classList.add("btn");
    saveBtn.innerText = "Save";
    saveBtn.addEventListener('click', function() {
        editGift(id);
        closeModal();
    })
    menu.appendChild(saveBtn);

    let closeBtn = document.createElement('button');
    closeBtn.classList.add("btn");
    closeBtn.innerText = "Close";
    closeBtn.addEventListener('click', function() {
        closeModal();
    })
    menu.appendChild(closeBtn);


    titleInput.addEventListener("keyup", function() {
        let Input = titleInput.value;
        if (Input != "") {
            saveBtn.removeAttribute("disabled");
        } else {
            saveBtn.setAttribute("disabled", null);
        }
    });

    modal.appendChild(modalTitle);

    form.appendChild(titleLabel);
    let br1 = document.createElement('br');
    form.appendChild(br1);
    form.appendChild(titleInput);
    let br2 = document.createElement('br');
    form.appendChild(br2);
    form.appendChild(descriptLabel);
    let br3 = document.createElement('br');
    form.appendChild(br3);
    form.appendChild(descriptTextarea);
    let br4 = document.createElement('br');
    form.appendChild(br4);
    modal.appendChild(form);

    modal.appendChild(menu);
}


function openView(id, title, description) 
{
    modalView.style.display = "block";
    document.body.style.positon = "fixed";

    let modal = document.getElementById("modalView-info");
    while(modal.firstChild) 
      modal.removeChild(modal.firstChild);

    let modalTitle = document.createElement('h1');
    modalTitle.innerText = title;
    modalTitle.classList.add("modal-title");

    let P = document.createElement('p');
    P.innerText = "Description";
    P.classList.add("view-modal-descript");

    let modalDescript = document.createElement('p');
    modalDescript.innerText = description;

    let menu = document.createElement('div');
    menu.classList.add("modal-menu");

    let editBtn = document.createElement('button');
    editBtn.classList.add("btn");
    editBtn.innerText = "Edit";
    editBtn.addEventListener('click', function() {
        editViewModal(id, title, description);
    })
    menu.appendChild(editBtn);

    let closeBtn = document.createElement('button');
    closeBtn.classList.add("btn");
    closeBtn.innerText = "Close";
    closeBtn.addEventListener('click', function() {
        closeModal();
    })
    menu.appendChild(closeBtn);

    modal.appendChild(modalTitle);
    modal.appendChild(P);
    modal.appendChild(modalDescript);
    modal.appendChild(menu);
}

function closeModal() 
{
    document.body.style.position = "absolute";
    modalSettings.style.display = "none";
    modalView.style.display = "none";
    modalAdd.style.display = "none";
}


// Create and append title and description DOM tags
function appendToDOM(gifts) 
{   //remove list if it exists
    while(giftList.firstChild) 
        giftList.removeChild(giftList.firstChild);
    
    //create and append tags
    for(let i = 0; i < gifts.length; i++) 
    {   
        //create title object
        let giftTitle = document.createElement('div');
        giftTitle.innerText = gifts[i].title;
        giftTitle.classList.add("gift-cap");
        giftTitle.addEventListener('click', function() 
        {
            openView(gifts[i].id, gifts[i].title, gifts[i].description);
        });
        //butonul de erase item
        let eraseBtn = document.createElement('button');
        eraseBtn.innerText = 'Erase';
        eraseBtn.classList.add("btn");
        //add event on btn and pass gift object
      eraseBtn.addEventListener('click', function() 
        {
            deleteGift(gifts[i].id);
        });  

        let li = document.createElement('li');
        li.appendChild(giftTitle);
        li.appendChild(eraseBtn);
        li.classList.add("gift-elem");

        giftList.appendChild(li);
    }
}


//afisarea lista cu items
function getGifts() 
{
    fetch('http://localhost:3000/gifts')
        .then(function(response) {
            response.json().then(function(gifts) {
                appendToDOM(gifts);
            });
        });
}

//adaugare new item
function postGift() {
    const gift = {
        title: formTitle.value,
        description: formDesc.value
    };
    fetch('http://localhost:3000/gifts', {
        method: 'post',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(gift)
    }).then(function() {
        getGifts();
        resetForm();
    });
}

//adaugare new item pt mobil
function postMGift() 
{
    let giftTitle1 = document.getElementById("modal-b-title").value;
    let giftDesc1 = document.getElementById("modal-b-descript").value;

    const gift = 
    {
        title: giftTitle1,
        description: giftDesc1
    };
    
    fetch('http://localhost:3000/gifts', {
        method: 'post',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(gift)
    }).then(function() {
        getGifts();  
    });
    closeModal();
   
}

//functie pt editarea unui cadou
function editGift(id) 
{
    const gift = 
    {
        title: document.getElementById('edit-b-title').value,
        description: document.getElementById('edit-b-descript').value
    }
    fetch(`http://localhost:3000/gifts/${id}`, {
        method: 'PUT',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(gift)
    }).then(function () {
        getGifts();
    });
}

//functie pt stergerea unui cadou
function deleteGift(id) 
{
    fetch(`http://localhost:3000/gifts/${id}`, {
        method: 'DELETE'
    }).then(function() {
        getGifts();
    });
}

//ResetForm
function resetForm() {
    formTitle.value = "";
    formDesc.value = "";
  }

//functie pt butonul de home, ca sa afiseze lista cu items
function openHome(){
    getGifts();
} 

//functia pentru deschiderea paginii cu info despre app
function openInfo(){
    while(giftList.firstChild) 
    giftList.removeChild(giftList.firstChild);

    let paragraph = document.createElement('p');
    paragraph.textContent = "This project was developed with those who take too long to take any decision ever in mind.Now you have the tool to actually change what you want every time you change your mind and be able to delete the items you no longer want or already have.Isn't it amazing? Moreover, you won' t get any more annoyed looks every time someone asks you what you want for Christmas and you don' t know what to answer.If you're feeling brave you might even save some bucketList items anf fullfill them yourself.The possibilities are endless. ";
    giftList.appendChild(paragraph);
   

}
getGifts();