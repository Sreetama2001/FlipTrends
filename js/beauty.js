fetch('https://fakestoreapi.com/products').then(res => res.json()).then(data => {
    let completeData = "";
    data.map(val => {
        image = val.image;
        completeData +=
            `<div class="card mb-3 m-3 card-deck" style="max-width: 500px; box-shadow: 10px 10px 5px 0px rgb(71, 68, 68); " id="category_card">
                        <div class="row no-gutters"  >
                        <div class="col-md-6 d-flex align-items-center justify-content-center" >
                            <a href="">
                                <img  src= ${val.image} class="card-img p-2" alt="..." height="300px">
                            </a>
                        </div>
                        <div class="col-md-6 d-flex align-items-center justify-content-center">
                            <div class="card-body">
                            <h5 class="card-title text-center"><span style="color:#898989;font-weight: bold;font-size:xx-large;">#</span><b  style="color:#282c34">1</b></h5>
                            <h3 class="card-title  text-center" style="color:#282c34;font-weight: bold; ">Subcategory</h3>
                            <p class="card-text text-center d-flex flex-wrap justify-content-center">
                                <button type="button" class="btn btn-secondary badge" data-toggle="tooltip" data-placement="right">
                               ${val.category}
                            </button>
                                <button type="button" class="btn btn-secondary badge" data-toggle="tooltip" data-placement="right">
                                ${val.price}
                                </button>
                                <button type="button" class="btn btn-secondary badge" data-toggle="tooltip" data-placement="right">
                                ${val.title}
                                </button>
                                <button type="button" class="btn btn-secondary badge" data-toggle="tooltip" data-placement="bottom">
                                ${val.category}
                                </button>                    
                            </p>
                            <p style="color:#282c34;font-weight:bolder;font-size:20px;line-height: initial;">See the matched product</p>
                            <div class="text-center" >
                            <p style="color:#282c34;font-weight:bolder;font-size:x-large;" aria-hidden="true"> 
                            <a href="www.google.com">
                                <i class="fa fa-external-link p-3"  style="background-color:#61dafb;color:#282c34;border-radius:4px; 
                                box-shadow: 10px 10px 5px 0px rgb(71, 68, 68);">
                                </i>
                            </a>
                             </p>
                            </div>
                            
                            
                            </div>
                        </div>
                        </div>
             </div>`
    });
    document.getElementById("cards").innerHTML = completeData;
});
