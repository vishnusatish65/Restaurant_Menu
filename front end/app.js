//on loading adding category
let category = []
let items = []
let page = 0
let total_no = 0
const Http = new XMLHttpRequest();
const url = "http://127.0.0.1:5000/menu/"
Http.open("GET",url)
Http.send()
Http.onreadystatechange = (e) => {
    if (Http.readyState==XMLHttpRequest.DONE){
        category = JSON.parse(Http.responseText).categories
        items = JSON.parse(Http.responseText).items
        items_total = JSON.parse(Http.responseText).items_total
        for(var i = 0; i < category.length; i++){
            if (i == 0){
                $(".list-group").append("<button class='category list-group-item active'>" + category[i] + "</button>")
                document.querySelector(".category-name").textContent = category[i]
                document.querySelector(".number-items") .textContent = items.length
                document.querySelector(".total-items") .textContent = items_total
                total_no = items_total
            }
            else{
                $(".list-group").append("<button class='category list-group-item'>" + category[i] + "</button>")
            }
        }
        add_items(items)
        // highlighting the active category
        category_active = document.querySelectorAll(".category")
        for (var i = 0; i < category_active.length; i++){
            category_active[i].addEventListener("click",makeactive)
        }
    }
}


function makeactive(){
    // function to change active class for buttons
    for (var i = 0; i < category_active.length; i++){
        category_active[i].classList.remove("active")
    }
    this.classList.add("active")
    removeItems() //removing old items
    document.querySelector(".switch-input").checked= false
    let active_list = []
    const Http = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/menu?" + "category_table=" + this.innerHTML
    Http.open("GET",url)
    Http.send()
    Http.onreadystatechange = (e) => {
        if (Http.readyState==XMLHttpRequest.DONE){
            active_list = JSON.parse(Http.responseText).items
            items_total = JSON.parse(Http.responseText).items_total
        }
      
    document.querySelector(".category-name").textContent = this.textContent
    document.querySelector(".number-items") .textContent = active_list.length
    document.querySelector(".total-items") .textContent = items_total
    add_items(active_list)
    }

    
}

//adding event listener to veg only checkbox and updating items div
document.querySelector(".switch-input").addEventListener("click",function(e){
    removeItems()
    let veg_list = []
    active_category = document.querySelector(".active").innerHTML
    const Http = new XMLHttpRequest();
    let url = ""
    if (this.checked == true){
        url = "http://127.0.0.1:5000/menu?" + "category_table=" + active_category + "&veg_only=veg" 
    }else{
        url = "http://127.0.0.1:5000/menu?" + "category_table=" + active_category
    }
    Http.open("GET",url)
    Http.send()
    Http.onreadystatechange = (e) => {
        if (Http.readyState==XMLHttpRequest.DONE){
            veg_list = JSON.parse(Http.responseText).items
            items_total = JSON.parse(Http.responseText).items_total
        }
    add_items(veg_list) 
    document.querySelector(".number-items") .textContent = veg_list.length
    document.querySelector(".total-items") .textContent = items_total
    }
})

// adding card elements
function add_items(list){
    for (var i = 0; i < list.length; i++){
    
        var card = document.createElement("div") //creating card element
        card.setAttribute("class", "card col-9")

        var header = document.createElement("div") // creating card header and sub nodes
        header.setAttribute("class","card-header-style")
        var header_item_sequence = document.createElement("span") 
        header_item_sequence.setAttribute("class","mr-auto item-sequence")
        header_item_sequence.innerText = list[i]["item_sequence"]
        header.appendChild(header_item_sequence)

        var available = document.createElement("span")
        available.setAttribute("class","availability")
        available.innerText = list[i]["available"]
        header.appendChild(available)
        card.appendChild(header)

        var body = document.createElement("div") //creating card body and sub nodes
        body.setAttribute("class","card-body")
        var card_title = document.createElement("h5") //card title
        card_title.setAttribute("class","card-title")
        card_title.innerText = list[i].name
        body.appendChild(card_title)

        var price =document.createElement("span")
        price.setAttribute("class","card-price")
        price.innerText = list[i].price + " Rs"
        body.appendChild(price)


        var description = document.createElement("p") //card description
        description.setAttribute("class","card-text")
        description.innerText = list[i].description
        body.appendChild(description)

        var swiggy = document.createElement('a') //adding swiggy and zomato details
        swiggy.setAttribute("class", "btn btn-swiggy")
        swiggy.innerText = "Swiggy"
        body.appendChild(swiggy)
        var zomato = document.createElement('a')
        zomato.setAttribute("class", "btn btn-zomato")
        zomato.innerText = "Zomato"
        body.appendChild(zomato)
        card.appendChild(body)

        document.querySelector(".item-display").appendChild(card)
        
    }

}

// remove child function
function removeItems(){
    while(document.querySelector(".item-display").firstChild){
        document.querySelector(".item-display").removeChild(document.querySelector(".item-display").firstChild)
    }
}


//next pagination
document.querySelector(".next").addEventListener("click",function(){

    page+=1
    removeItems()
    let current_list = []
    active_category = document.querySelector(".active").innerHTML
    const Http = new XMLHttpRequest();
    let url = ""
    if (document.querySelector(".switch-input").checked == true){
        url = "http://127.0.0.1:5000/menu?" + "category_table=" + active_category + "&veg_only=veg&page="+page
    }else{
        url = "http://127.0.0.1:5000/menu?" + "category_table=" + active_category + "&page="+ page
    }
    Http.open("GET",url)
    Http.send()
    Http.onload = (e) => {
        if (Http.status==200){
            current_list = JSON.parse(Http.responseText).items
            items_total = JSON.parse(Http.responseText).items_total
        }
    if (current_list.length > 0){
        add_items(current_list)
    }else{
        var message = document.createElement("h1")
        message.innerHTML = "No more items to show!!!!"
        document.querySelector(".item-display").appendChild(message)
    }
    
    document.querySelector(".number-items") .textContent = current_list.length
    document.querySelector(".total-items") .textContent = items_total
    }
    

})

//previous pagination
document.querySelector(".previous").addEventListener("click",function(){
    if (page>0){
        page-=1
        removeItems()
        let current_list = []
        active_category = document.querySelector(".active").innerHTML
        const Http = new XMLHttpRequest();
        let url = ""
        if (document.querySelector(".switch-input").checked == true){
            url = "http://127.0.0.1:5000/menu?" + "category_table=" + active_category + "&veg_only=veg&page="+page 
        }else{
            url = "http://127.0.0.1:5000/menu?" + "category_table=" + active_category + "&page="+page
        }
        Http.open("GET",url)
        Http.send()
        Http.onreadystatechange = (e) => {
            if (Http.readyState==XMLHttpRequest.DONE){
                current_list = JSON.parse(Http.responseText).items
                items_total = JSON.parse(Http.responseText).items_total
            }
        add_items(current_list)
        document.querySelector(".number-items") .textContent = current_list.length
        document.querySelector(".total-items") .textContent = items_total
        }
        
    }
})

document.querySelector(".search").addEventListener("input",function(e){
    page = 0
    data = e.target.value
    removeItems()
    let current_list = []
    active_category = document.querySelector(".active").innerHTML
    const Http = new XMLHttpRequest();
    let url = ""
    if (document.querySelector(".switch-input").checked == true){
        url = "http://127.0.0.1:5000/menu/search?" + "category_table=" + active_category + "&veg_only=veg&page="+page +"&search="+data
    }else{
        url = "http://127.0.0.1:5000/menu/search?" + "category_table=" + active_category + "&page="+ page +"&search="+data
    }
    console.log(url)
    Http.open("GET",url)
    Http.send()
    Http.onload = (e) => {
        if (Http.status==200){
            current_list = JSON.parse(Http.responseText).items
            items_total = JSON.parse(Http.responseText).items_total
        }
    if (current_list.length > 0){
        add_items(current_list)
    }else{
        var message = document.createElement("h1")
        message.innerHTML = "No Matches found!!!!"
        document.querySelector(".item-display").appendChild(message)
    }
    
    document.querySelector(".number-items") .textContent = current_list.length
    document.querySelector(".total-items") .textContent = items_total
    }
    

})

