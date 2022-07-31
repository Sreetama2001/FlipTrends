//Data fetch from API
function fetching() {
    
    let url = "https://ap-south-1.aws.data.mongodb-api.com/app/api-smznw/endpoint/kids?secret=new";
    fetch(url)
        .then(res => res.json()).then(data => {
            console.log(data);
            data.sort((a, b) => {
                return b.trend_score - a.trend_score;
            });
            addData(data);
        });
}
fetching();
//Add Chart and cards in html
function addData(data) {

    if (data.length > 0) {
        renderData(data)
    }
    else {
        showPopUp();
    }
}
//show pop up if API is empty
function showPopUp() {
    swal({
        title: "OOPS",
        text: "Nothing is trending right now in this category",
        icon: "warning",
        closeOnClickOutside: false,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                window.location = "./index.html";
            }
        });
}
//render data array
function renderData(data) {
    let completeData = "";
    let count = 1;
    let xlabelsArray = [];
    let ylabelsArray = [];
    data.map(val => {
        let subCategory = ((val.sub_category == null) || (val.sub_category == undefined)) ? "" : val.sub_category;
        let trendingScore = ((val.trend_score == null) || (val.trend_score == undefined)) ? "" : val.trend_score;
        let vertical = ((val.vertical == null) || (val.vertical == undefined)) ? "" : `<button type="button" class="btn btn-secondary badge" 
        data-toggle="tooltip" data-placement="right">
        ${val.vertical}
        </button>`;
        let type = ((val.attribute_type == null) || (val.attribute_type == undefined)) ? "" : `<button type="button" class="btn btn-secondary badge" 
        data-toggle="tooltip" data-placement="right">
        ${val.attribute_type}
        </button>`;
        let value = ((val.attribute_value == null) || (val.attribute_value == undefined)) ? "" : `<button type="button" class="btn btn-secondary badge" data-toggle="tooltip" data-placement="right">
        ${val.attribute_value}
        </button>`;
        let postImg = ((val.image_url == null) || (val.image_url == undefined)) ? `${val.post_url}` : val.image_url;

        xlabelsArray.push(val.sub_category);

        ylabelsArray.push(count);

        completeData +=
            `<div class="card mb-3 m-3 card-deck d-flex justify-content-center" style="max-width: 500px; box-shadow: 10px 10px 5px 0px rgb(71, 68, 68); " id="category_card">
            <div class="row no-gutters"  >
                <div class="col-md-6 d-flex align-items-center justify-content-center" >
                    <div class="img-area">
                    <a href=${val.post_url}>
                        <img  src=${postImg} class="card-img py-2 image" alt="..." height="300px">
                    </a>
                        <div class="overlay">
                            <div class="image-text"> 
                                <div class="text-center" >
                                    <p style="color:#282c34;font-weight:bolder;font-size:small;" aria-hidden="true">
                                    <a href="${val.post_url}">
                                        <i class="fa fa-external-link p-3"  style="font-size:large;background-color:white;color:#282c34;border-radius:4px; 
                                        box-shadow: 10px 10px 5px 0px rgb(71, 68, 68);">
                                        </i>
                                    </a>
                                    </p>
                                    <p class="text-center p-1" style="color:white;font-weight:bolder;font-size:15px;line-height: initial;">See the post</p>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
            <div class="col-md-6 d-flex align-items-center justify-content-center">
                <div class="card-body">
                    <h5 class="card-title text-center"><span style="color:#898989;font-weight: bold;font-size:xx-large;">#</span><b  style="color:#282c34">${count++}</b></h5>
                    <h4 class="card-title  text-center" style="color:#282c34;font-weight: bold; ">${subCategory}</h4>
                    <p class="card-title  text-center" style="color:#282c34;font-weight: bold; ">Trending Score:${trendingScore}</p>
                    <p class="card-text text-center d-flex flex-wrap justify-content-center">
                    ${vertical}
                    ${type}
                    ${value}
                    </p>
                    <p class="text-center p-1" style="color:#282c34;font-weight:bolder;font-size:15px;line-height: initial;">See the matched product</p>
                    <div class="text-center" >
                    <p style="color:#282c34;font-weight:bolder;font-size:x-large;" aria-hidden="true">
                    <a href="${val.flipkart_url}">
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
    addChart(data, xlabelsArray, ylabelsArray);
    document.getElementById("cards").innerHTML = completeData;
}
//add chart
function addChart(data, xlabelsArray, ylabelsArray) {
    document.getElementById("chart-section").innerHTML = `
    <div class="row p-4  d-flex justify-content-evenly" id="chart-bg">
      <div id="chart-heading" class="col-md-12 text-center" >Trends Analysis & Trending Keywords</div>
      <div class="col-md-6 d-flex align-items-center"  id="Chart" max-height="400">
        <canvas id="myChart"class="p-3"></canvas>
      </div>
      <div class="col-md-4 p-3">
      <div>
      <li class="list-group-item p-3 text-center" id="trendKeywordHeading">Trending Keywords</li>
      <ul class="list-group" id="keyword-list">
     </ul>
      </div>
    </div>
  </div>
    `;
    chartMake(xlabelsArray, ylabelsArray);
    trendsKeywords(data);
}
//make chart code from chart.js
function chartMake(xlabelsArray, ylabelsArray) {
    let ctx = document.getElementById('myChart').getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'line',

        data: {
            labels: xlabelsArray,
            datasets: [{
                label: 'Trending product ranking Vs Subcategory',
                data: ylabelsArray,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor:
                    'rgba(255, 99, 132, 1)',
                borderWidth: 3,
                fill: true
            }]
        },
        options: {

            scales: {

                x: {
                    ticks: {
                        color: ["blue", "black", "red"],
                        maxRotation: 90,
                        minRotation: 90,
                        sampleSize: 4,
                        font: {
                            size: 10,

                        }
                    },

                },
                y: {
                    ticks: {
                        min: 1,
                        sampleSize: 15,
                        color: ["blue", "black", "red"],
                        font: {
                            size: 20,
                        }
                    },

                    beginAtZero: false,
                }
            }
        }
    });

}
//Top trending rending keywords
function trendsKeywords(data) {
    let keywordList = "";
    for (let i = 0; i <= 4; i++) {

        keywordList += `<li class="list-group-item keyword-item">${data[i].keyword}</li>`;
    }

    document.getElementById("keyword-list").innerHTML = keywordList;
}
//fetch data after given interval
setInterval(fetching, 2700000);