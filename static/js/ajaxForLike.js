function like(slug , id){
    let element = document.getElementById("status")
    let count = document.getElementById("count")
    $.get(`/article/like/${slug}/${id}`).then(response =>
    {
        if(response['response']==="liked"){
            element.className = "fa fa-heart"
            count.innerText = Number(count.innerText) + 1
        }else{
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) - 1
        }
    }
    )
}